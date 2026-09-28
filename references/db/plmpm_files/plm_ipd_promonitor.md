# 监控-plm_ipd_promonitor

## 监控-主表 t_plm_ipd_promonitor

- **表名称：** 监控-主表
- **表名：** t_plm_ipd_promonitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdata_values | 数值 | numeric | 23 | 2 | √ | 0 | 数值 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmonitoring_item | 监控项 | varchar | 50 |  | √ | ' ' | 监控项 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | frelated_parameters | 相关参数 | varchar | 50 |  | √ | ' ' | 相关参数 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fadminorg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | findicator | 指标 | varchar | 50 |  | √ | ' ' | 指标 |
| 13 | flights | 红绿灯指示 | varchar | 50 |  | √ | ' ' | 红绿灯指示,枚举: R :红色图标 G :绿色图标 Y :黄色图标 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_promonitor |  | fid |
| 2 | idx_plm_ipd_promonitor_m0 |  | fbillno |

---

## 监控-多语言表 t_plm_ipd_promonitor_l

- **表名称：** 监控-多语言表
- **表名：** t_plm_ipd_promonitor_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelated_parameters | frelated_parameters | varchar | 500 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | findicator | 指标 | varchar | 500 |  | √ | ' ' | 指标 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fmonitoring_item | 监控项 | varchar | 500 |  | √ | ' ' | 监控项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_promonitor_l |  | fpkid |
| 2 | idx_plm_ipd_promonitor_l_0 |  | fid,flocaleid |

---

## 单据体-子表 t_plm_ipd_monitorentry

- **表名称：** 单据体-子表
- **表名：** t_plm_ipd_monitorentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstandard | 标准 | varchar | 500 |  | √ | ' ' | 标准 |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fall_lights |  | varchar | 50 |  | √ | ' ' | ,枚举: R :红色图标 G :绿色图标 Y :黄色图标 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_monitorentry_fk |  | fid |
| 2 | pk_plm_ipd_monitorentry |  | fentryid |
