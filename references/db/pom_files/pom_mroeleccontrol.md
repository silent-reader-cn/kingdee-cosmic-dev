# 检修断路器控制单-pom_mroeleccontrol

## 关联子实体-子表 t_pom_mroeleccontrol_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mroeleccontrol_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mroeleccontrol_lk_fk |  | fid |
| 2 | pk_pom_mroeleccontrol_lk |  | fpkid |

---

## 检修断路器控制单-关联追踪表 t_pom_mroeleccontrol_tc

- **表名称：** 检修断路器控制单-关联追踪表
- **表名：** t_pom_mroeleccontrol_tc

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
| 1 | pk_pom_mroeleccontrol_tc |  | fid |
| 2 | idx_pom_mroeleccontrol_tc_tbill |  | ftbillid |
| 3 | idx_pom_mroeleccontrol_tc_tid |  | ftid |

---

## 标识信息-子表 t_pom_mroelecsubentry

- **表名称：** 标识信息-子表
- **表名：** t_pom_mroelecsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fisremove | 是否移除 | bpchar | 1 |  | √ | '0' | 是否移除 |
| 2 | ftagcreatetime | 标识创建时间 | timestamp | 0 |  |  | null | 标识创建时间 |
| 3 | ftagmodifytime | 标识移除时间 | timestamp | 0 |  |  | null | 标识移除时间 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fphonenum | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 6 | forderno | 检修工单编号 | varchar | 50 |  | √ | ' ' | 检修工单编号 |
| 7 | fworkdescription | 工作内容描述 | varchar | 255 |  | √ | ' ' | 工作内容描述 |
| 8 | fcblocation | 断路器位置 | varchar | 50 |  | √ | ' ' | 断路器位置 |
| 9 | fcardname | 工卡标题 | varchar | 255 |  | √ | ' ' | 工卡标题 |
| 10 | fuserfield | 员工工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fpanel | 面板 | varchar | 50 |  | √ | ' ' | 面板 |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fworkcardname | 工卡 | int8 | 64 |  | √ | 0 | [工卡维护 mpdm_workcards](../mpdm_files/mpdm_workcards.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fprofession | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 16 | ftagcreater | 标识创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftagmodifier | 标识移除人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mroelecsubentry_fk |  | fentryid |
| 2 | pk_pom_mroelecsubentry |  | fdetailid |

---

## 检修断路器控制单-主表 t_pom_mroeleccontrol

- **表名称：** 检修断路器控制单-主表
- **表名：** t_pom_mroeleccontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftransactiontype | 生产事务类型 | int8 | 64 |  | √ | 0 | [生产事务类型 mpdm_transactproduct](../mpdm_files/mpdm_transactproduct.md) |
| 4 | fworkcardid | 工卡号 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |
| 5 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | forderentryid | 检修工单行号 | int8 | 64 |  | √ | 0 | [检修工单分录F7 pom_mroorder_f7](../pom_files/pom_mroorder_f7.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | faircraftregistnum | 飞机注册号 | int8 | 64 |  | √ | 0 | [检修等级 mpdm_checklevel](../mpdm_files/mpdm_checklevel.md) |
| 9 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ffinemodel | 精细机型 | int8 | 64 |  | √ | 0 | [检修设备型号 mpdm_over_device_number](../mpdm_files/mpdm_over_device_number.md) |
| 12 | forderstatus | 检修工单状态 | varchar | 50 |  | √ | ' ' | 检修工单状态 |
| 13 | fmaintrade | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 14 | fmaterialmtcinfo | 物料检修信息 | int8 | 64 |  | √ | 0 | [物料检修信息 mpdm_materialmtcinfo](../mpdm_files/mpdm_materialmtcinfo.md) |
| 15 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 16 | fprojectcreatedate | 项目创建时间 | timestamp | 0 |  |  | null | 项目创建时间 |
| 17 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fmratype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | forderno | 检修工单编号 | varchar | 50 |  | √ | ' ' | 检修工单编号 |
| 26 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 30 | fcbstatus | 断路工具状态 | varchar | 50 |  | √ | ' ' | 断路工具状态,枚举: F :闭合 N :打开 |
| 31 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mroeleccontrol_fbillno |  | fbillno |
| 2 | pk_pom_mroeleccontrol |  | fid |

---

## 关联子实体-子表 t_pom_mroeleccontrolcb_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mroeleccontrolcb_lk

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
| 1 | pk_pom_mroeleccontrolcb_lk |  | fpkid |
| 2 | idx_pom_mroeleccontrolcb_lk_fk |  | fentryid |

---

## 检修断路器控制单-反写记录表 t_pom_mroeleccontrol_wb

- **表名称：** 检修断路器控制单-反写记录表
- **表名：** t_pom_mroeleccontrol_wb

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
| 1 | pk_pom_mroeleccontrol_wb |  | fentryid |
| 2 | idx_pom_mroeleccontrol_wb_fk |  | fid |

---

## 断路器信息-子表 t_pom_mroelecentry

- **表名称：** 断路器信息-子表
- **表名：** t_pom_mroelecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftagcounttext | 标识数量 | varchar | 30 |  | √ | ' ' | 标识数量 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ftagcountden | 标识总数 | int8 | 64 |  | √ | 0 | 标识总数 |
| 5 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :手工新增 B :来源工卡 |
| 7 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fcblocation | 断路器位置 | varchar | 50 |  | √ | ' ' | 断路器位置 |
| 9 | fcbname | 断路器名称 | varchar | 50 |  | √ | ' ' | 断路器名称 |
| 10 | fcbtoolstatus | 断路工具状态 | varchar | 50 |  | √ | ' ' | 断路工具状态,枚举: OFF :闭合 ON :打开 |
| 11 | ftagcountmol | 当前标识数 | int8 | 64 |  | √ | 0 | 当前标识数 |
| 12 | fpanel | 面板 | varchar | 50 |  | √ | ' ' | 面板 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fismodify | 修改标识 | bpchar | 1 |  | √ | '0' | 修改标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mroelecentry_fk |  | fid |
| 2 | pk_pom_mroelecentry |  | fentryid |
