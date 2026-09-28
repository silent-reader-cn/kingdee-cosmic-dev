# 数据健康巡查-ap_healthcheck

## 单据体-子表 t_ap_healthchecksentry

- **表名称：** 单据体-子表
- **表名：** t_ap_healthchecksentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrormessage | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 3 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 7 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_healthchecksentry_fid |  | fid |
| 2 | pk_t_ap_healthchecksentry |  | fentryid |

---

## 数据健康巡查-主表 t_ap_healthchecks

- **表名称：** 数据健康巡查-主表
- **表名：** t_ap_healthchecks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 应付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fexecutestatus | 执行状态 | varchar | 30 |  | √ | '0' | 执行状态,枚举: 0 :未执行 1 :执行中 2 :执行成功 3 :执行失败 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fcheckitemid | 巡查项 | int8 | 64 |  | √ | 0 | [数据巡查项 ap_datacheck_item](../ap_files/ap_datacheck_item.md) |
| 9 | fbizappid | 应用 | varchar | 30 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmorefilterval_tag | 更多过滤条件_详情 | text | 0 |  |  | null | 更多过滤条件_详情 |
| 12 | fenddate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 13 | fdetail | 详细信息 | varchar | 255 |  | √ | ' ' | 详细信息 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fstartdate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 16 | fbillentityid | 被巡查单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 17 | fmorefilterval | 更多过滤条件 | varchar | 255 |  | √ | ' ' | 更多过滤条件 |
| 18 | fchecktime | 检查时间 | timestamp | 0 |  |  | null | 检查时间 |
| 19 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fcheckstatus | 检查状态 | varchar | 30 |  | √ | '0' | 检查状态,枚举: 0 :未知 1 :正常 2 :异常 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_healthchecks_fbillno |  | fbillno |
| 2 | pk_t_ap_healthchecks |  | fid |

---

## 多选组织-多选基础资料表 t_ap_healthchecksorgs

- **表名称：** 多选组织-多选基础资料表
- **表名：** t_ap_healthchecksorgs

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
| 1 | idx_ap_healthchecksorgs_fid |  | fid |
| 2 | pk_t_ap_healthchecksorgs |  | fpkid |
