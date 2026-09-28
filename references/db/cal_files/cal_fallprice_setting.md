# 存货跌价准备设置-cal_fallprice_setting

## 单据体-子表 t_cal_fallpricesetentry

- **表名称：** 单据体-子表
- **表名：** t_cal_fallpricesetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 7 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 8 | finvagefrom | 库龄从（天） | int8 | 64 |  | √ | 0 | 库龄从（天） |
| 9 | fwarehousegroupid | 仓库分组 | int8 | 64 |  | √ | 0 | [仓库分组 bd_warehousegroup](../sbd_files/bd_warehousegroup.md) |
| 10 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fownertype | 货主类型 | varchar | 80 |  | √ | 'bos_org' | 货主类型,枚举: bos_org :核算组织 bd_customer :客户 bd_supplier :供应商 |
| 12 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 13 | funitrealizableamount | 单位可变现净值 | numeric | 23 | 10 | √ | 0.0000000000 | 单位可变现净值 |
| 14 | flot | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 15 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 17 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 18 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 19 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 21 | fexpirydateto | 剩余有效期至（天） | int4 | 32 |  | √ | 999999 | 剩余有效期至（天） |
| 22 | ffallpricescale | 存货跌价比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 存货跌价比例(%) |
| 23 | fexpirydatefrom | 剩余有效期从（天） | int4 | 32 |  | √ | '-999999' | 剩余有效期从（天） |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | finvageto | 库龄至（天） | int8 | 64 |  | √ | 0 | 库龄至（天） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_fallpricee_id |  | fid |
| 2 | t_cal_fallpricesetentry_pkey |  | fentryid |
| 3 | idx_cal_fallpricesete_mat |  | fmaterialid |

---

## 存货跌价准备设置-多语言表 t_cal_fallpricesetting_l

- **表名称：** 存货跌价准备设置-多语言表
- **表名：** t_cal_fallpricesetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_fallpricesetl_local |  | fid,flocaleid |
| 2 | t_cal_fallpricesetting_l_pkey |  | fpkid |

---

## 存货跌价准备设置-主表 t_cal_fallpricesetting

- **表名称：** 存货跌价准备设置-主表
- **表名：** t_cal_fallpricesetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fnotcalagebill | 不参与账龄统计的单据 | int8 | 64 |  | √ | 0 | [不参与账龄统计的单据 cal_notcalage](../cal_files/cal_notcalage.md) |
| 4 | fapprovetime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 5 | fprovisionway | 计提方式 | bpchar | 1 |  | √ | 'A' | 计提方式,枚举: A :物料 B :物料分类 C :仓库分组 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsetdimension | 设置维度 | varchar | 255 |  | √ | 'A' | 设置维度,枚举: x :物料 owner :货主 storageorgunit :库存组织 warehouse :仓库 location :仓位 assist :辅助属性 lot :批号 mversion :物料版本 invtype :库存类型 invstatus :库存状态 project :项目编码 configuredcode :配置号 tracknumber :跟踪号 |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 12 | fenableshelflife | 保质期物料按有效期设置 | bpchar | 1 |  | √ | '0' | 保质期物料按有效期设置 |
| 13 | fprovisiontomat | 计提到物料 | bpchar | 1 |  | √ | '0' | 计提到物料 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmaterialgroupstandard | 物料分类标准 | int8 | 64 |  | √ | 0 | [物料分类标准 bd_materialgroupstandard](../basedata_files/bd_materialgroupstandard.md) |
| 18 | faccsysid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系（已作废） bd_accountingsys](../fibd_files/bd_accountingsys.md) |
| 19 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 cal_bd_calpolicy](../cal_files/cal_bd_calpolicy.md) |
| 20 | fmaximumage | 最大账龄 | int8 | 64 |  | √ | 0 | 最大账龄 |
| 21 | fprovstrategy | 计提策略 | bpchar | 1 |  | √ | 'A' | 计提策略,枚举: A :按月度 B :按季度 C :按半年 D :按年度 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 24 | fprovdimension | 计提维度 | varchar | 1000 |  | √ | ' ' | 计提维度,枚举: owner :货主 storageorgunit :库存组织 warehouse :仓库 location :仓位 assist :辅助属性 lot :批号 mversion :物料版本 project :项目编码 invtype :库存类型 invstatus :库存状态 configuredcode :配置号 tracknumber :跟踪号 |
| 25 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_fallpricesetting_acct |  | fcostaccountid |
| 2 | t_cal_fallpricesetting_pkey |  | fid |
| 3 | idx_cal_fallpriceset_org |  | fcalorgid |
