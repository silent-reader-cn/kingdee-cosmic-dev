# 项目装箱单-mpm_projectencasement

## 关联子实体-子表 t_mpsm_encaseentity_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpsm_encaseentity_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpsm_encaseentity_lk |  | fpkid |
| 2 | idx_mpsm_encaseentity_lk_fk |  | fentryid |

---

## 物料明细-子表 t_mpm_encaseentity

- **表名称：** 物料明细-子表
- **表名：** t_mpm_encaseentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 6 | fdelivermaterialdes | 发货物资描述 | varchar | 255 |  | √ | ' ' | 发货物资描述 |
| 7 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 8 | fownertype | 货主类型 | varchar | 80 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 9 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 12 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 13 | fdeliveraddress | 发货地点 | varchar | 512 |  | √ | ' ' | 发货地点 |
| 14 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 15 | fdeliveraddresstype | 发货类型和地点 | bpchar | 1 |  | √ | ' ' | 发货类型和地点,枚举: A :生产现场-物料 C :生产现场-物资描述 B :仓库 |
| 16 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 17 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 18 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 20 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | frejectedqty | 已拒收数量 | numeric | 23 | 10 | √ | 0 | 已拒收数量 |
| 22 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 24 | fassotransportqty | 关联运输数量 | numeric | 23 | 10 | √ | 0 | 关联运输数量 |
| 25 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 26 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 27 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 29 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 30 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 33 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 34 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 35 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 36 | factrecqty | 已实收数量 | numeric | 23 | 10 | √ | 0 | 已实收数量 |
| 37 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 38 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 39 | fpointedbaseqty | 已点收基本数量 | numeric | 23 | 10 | √ | 0 | 已点收基本数量 |
| 40 | ftransportbaseqty | 已运输基本数量 | numeric | 23 | 10 | √ | 0 | 已运输基本数量 |
| 41 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 42 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 43 | ftransportqty | 已运输数量 | numeric | 23 | 10 | √ | 0 | 已运输数量 |
| 44 | frejectedbaseqty | 已拒收基本数量 | numeric | 23 | 10 | √ | 0 | 已拒收基本数量 |
| 45 | fpointedqty | 已点收数量 | numeric | 23 | 10 | √ | 0 | 已点收数量 |
| 46 | factrecbaseqty | 已实收基本数量 | numeric | 23 | 10 | √ | 0 | 已实收基本数量 |
| 47 | fproducttype | 产品类别 | varchar | 255 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 48 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 49 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 50 | fassotransportbaseqty | 关联运输基本数量 | numeric | 23 | 10 | √ | 0 | 关联运输基本数量 |
| 51 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 52 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_encaseentity_fid |  | fid |
| 2 | pk_mpm_encaseentity |  | fentryid |

---

## 项目装箱单-多语言表 t_mpm_proencase_l

- **表名称：** 项目装箱单-多语言表
- **表名：** t_mpm_proencase_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_proencase_l_fid |  | fid,flocaleid |
| 2 | pk_mpm_proencase_l |  | fpkid |

---

## 项目装箱单-关联追踪表 t_mpsm_proencase_tc

- **表名称：** 项目装箱单-关联追踪表
- **表名：** t_mpsm_proencase_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpsm_proencase_tc |  | fid |
| 2 | idx_mpsm_proencase_tc_tbill |  | ftbillid |
| 3 | idx_mpsm_proencase_tc_tid |  | ftid |

---

## 项目装箱单-反写记录表 t_mpsm_proencase_wb

- **表名称：** 项目装箱单-反写记录表
- **表名：** t_mpsm_proencase_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpsm_proencase_wb_fk |  | fid |
| 2 | pk_mpsm_proencase_wb |  | fentryid |

---

## 物料明细-多语言表 t_mpm_encaseentity_l

- **表名称：** 物料明细-多语言表
- **表名：** t_mpm_encaseentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdelivermaterialdes | 发货物资描述 | varchar | 255 |  | √ | ' ' | 发货物资描述 |
| 2 | fdeliveraddress | 发货地点 | varchar | 512 |  | √ | ' ' | 发货地点 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_encaseentity_l |  | fpkid |
| 2 | idx_mpm_encaseentity_l_fid |  | fentryid,flocaleid |

---

## 项目装箱单-主表 t_mpm_proencase

- **表名称：** 项目装箱单-主表
- **表名：** t_mpm_proencase

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpackmanagerid | 装箱负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fboxnum | 箱号 | varchar | 50 |  | √ | ' ' | 箱号 |
| 5 | fgroupnumid | 组号 | int8 | 64 |  | √ | 0 | [组号 mpm_groupnumber](../mpm_files/mpm_groupnumber.md) |
| 6 | fpacksupplierid | 包装供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftransvehibrand | 运输工具牌号 | varchar | 255 |  | √ | ' ' | 运输工具牌号 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fprojectheadid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 11 | fcontainernum | 集装箱号 | varchar | 255 |  | √ | ' ' | 集装箱号 |
| 12 | flogcontper | 物流联系人 | varchar | 255 |  | √ | ' ' | 物流联系人 |
| 13 | fboxcode | 箱码 | varchar | 255 |  | √ | ' ' | 箱码 |
| 14 | flogcompanyid | 物流公司 | int8 | 64 |  | √ | 0 | [物流公司 pur_logsupplier](../pbd_files/pur_logsupplier.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flogtracknum | 物流单号 | varchar | 255 |  | √ | ' ' | 物流单号 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fpackdate | 装箱日期 | timestamp | 0 |  |  | null | 装箱日期 |
| 23 | flogcontphone | 物流联系电话 | varchar | 50 |  | √ | ' ' | 物流联系电话 |
| 24 | fgrouprelid | 组号序号关联关系 | int8 | 64 |  | √ | 0 | [项目装箱单组号关联关系 mpm_encasegrouprel](../mpm_files/mpm_encasegrouprel.md) |
| 25 | flogistics | 启用运输 | bpchar | 1 |  | √ | '0' | 启用运输 |
| 26 | fexternalnum | 运输编号 | varchar | 100 |  | √ | ' ' | 运输编号 |
| 27 | fpointstatus | 点收状态 | bpchar | 1 |  | √ | 'A' | 点收状态,枚举: A :未点收 B :部分点收 C :已点收 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_proencase |  | fid |
| 2 | idx_mpm_proencase_bno |  | fbillno |
