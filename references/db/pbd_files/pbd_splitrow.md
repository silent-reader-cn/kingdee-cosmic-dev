# 拆分行配置-pbd_splitrow

## 单据体-子表 t_pur_splitrowentry

- **表名称：** 单据体-子表
- **表名：** t_pur_splitrowentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrentmetadata | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 3 | fcopyrow | 复制携带 | bpchar | 1 |  | √ | ' ' | 复制携带 |
| 4 | fcurrentmetadatakey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 5 | fsplitrow | 拆分携带 | bpchar | 1 |  | √ | ' ' | 拆分携带 |
| 6 | fdefaultvalue | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdefaultrow | 默认携带 | bpchar | 1 |  | √ | ' ' | 默认携带 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_splitrowentry |  | fentryid |
| 2 | idx_splitrowentry_fid_fseq |  | fid,fseq |

---

## 拆分行配置-主表 t_pur_splitrow

- **表名称：** 拆分行配置-主表
- **表名：** t_pur_splitrow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | frelationconfig | 关联配置前缀 | varchar | 50 |  | √ | ' ' | 关联配置前缀 |
| 6 | fentrykey | 分录标识 | varchar | 50 |  | √ | ' ' | 分录标识 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpluginname | 插件名称 | varchar | 255 |  | √ | ' ' | 插件名称 |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fbillkey | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_splitrow |  | fid |
| 2 | idx_pur_splitrow_fbillno |  | fbillno |
