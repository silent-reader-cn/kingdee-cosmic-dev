# MTO库存释放-mrp_mtoinvrelease

## MTO库存释放-主表 t_mrp_mtoinvrelease

- **表名称：** MTO库存释放-主表
- **表名：** t_mrp_mtoinvrelease

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ftotracknumber | 至 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_mtoinvrelease |  | fid |
| 2 | idx_mrp_mtoinvrelease_billno |  | fbillno |

---

## 物料-多选基础资料表 t_mrp_mtoinvrelease_mft

- **表名称：** 物料-多选基础资料表
- **表名：** t_mrp_mtoinvrelease_mft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_mtoinvrelease_mft |  | fpkid |
| 2 | idx_mrp_mtoinvrelease_mft_fid |  | fid |

---

## 跟踪号-多选基础资料表 t_mrp_mtoinvrelease_tra

- **表名称：** 跟踪号-多选基础资料表
- **表名：** t_mrp_mtoinvrelease_tra

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_mtoinvrelease_tra_fid |  | fid |
| 2 | pk_mrp_mtoinvrelease_tra |  | fpkid |

---

## 库存明细单据体-子表 t_mrp_mtoinvreleaseentry

- **表名称：** 库存明细单据体-子表
- **表名：** t_mrp_mtoinvreleaseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 5 | flocation | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fkeeper | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | forg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | finvtype | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 11 | fqtyavb | 可用库存数量 | numeric | 23 | 10 | √ | 0 | 可用库存数量 |
| 12 | funit3rd | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 14 | funit2nd | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 16 | fconvertqty | 转换数量 | numeric | 23 | 10 | √ | 0 | 转换数量 |
| 17 | finvqty | 库存数量 | numeric | 23 | 10 | √ | 0 | 库存数量 |
| 18 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 19 | fkeepertype | 保管者类型 | varchar | 30 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 20 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | fowner | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | finvid | 库存余额表id | int8 | 64 |  | √ | 0 | 库存余额表id |
| 23 | finvmaterial | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 24 | fqty2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 25 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 26 | fproject | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 28 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 29 | fqty3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 32 | funit | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | finvstatus | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_mtoinvreleaseentry |  | fentryid |
| 2 | idx_mrp_mtoinvreleaseentry_fid |  | fid |

---

## 仓库编码-多选基础资料表 t_mrp_mtoinvrelease_ware

- **表名称：** 仓库编码-多选基础资料表
- **表名：** t_mrp_mtoinvrelease_ware

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_mtoinvrelease_ware |  | fpkid |
| 2 | idx_mrp_mtoinvrelease_ware_fid |  | fid |

---

## 库存组织-多选基础资料表 t_mrp_mtoinvrelease_org

- **表名称：** 库存组织-多选基础资料表
- **表名：** t_mrp_mtoinvrelease_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_mtoinvrelease_org |  | fpkid |
| 2 | idx_mrp_mtoinvrelease_org_fid |  | fid |

---

## MTO转换单据体-子表 t_mrp_mtorlsconvertentry

- **表名称：** MTO转换单据体-子表
- **表名：** t_mrp_mtorlsconvertentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftfmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | ftfinvtype | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 4 | ftfbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftfexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 7 | ftfproject | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 8 | ftftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 9 | ftfownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 10 | ftfkeeper | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | ftfbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 12 | ftflotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 13 | ftfmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 14 | ftfbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | ftfunit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | ftfconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 17 | ftfmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 18 | fconvertqty | 转换数量 | numeric | 23 | 10 | √ | 0 | 转换数量 |
| 19 | ftfinvstatus | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 20 | ftfunit3rd | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | ftfconverttype | 转换类型 | bpchar | 1 |  | √ | 'A' | 转换类型,枚举: A :转换前 B :转换后 |
| 22 | ftfunit2nd | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | ftfproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 24 | ftforg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | ftfadjustbillid | 形态转换单id | int8 | 64 |  | √ | 0 | 形态转换单id |
| 26 | ftfkeepertype | 保管者类型 | varchar | 30 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 27 | ftfbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | finvmaterial | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 29 | ftfwarehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 30 | ftfqty3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 31 | ftflocation | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 32 | ftfowner | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | ftfqty2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | ftfauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 36 | ftfqty | 当前库存 | numeric | 23 | 10 | √ | 0 | 当前库存 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_mtorlsconvertentry_fid |  | fid |
| 2 | pk_mrp_mtorlsconvertentry |  | fentryid |
