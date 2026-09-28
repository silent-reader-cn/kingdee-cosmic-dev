# 条码解析日志-barcm_parselog

## 条码解析日志-主表 t_barcm_parselog

- **表名称：** 条码解析日志-主表
- **表名：** t_barcm_parselog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 描述信息 | varchar | 512 |  | √ | ' ' | 描述信息 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fbarcodevaluehead | 条码值 | varchar | 1000 |  | √ | ' ' | 条码值 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fparsestatus | 解析状态 | bpchar | 1 |  | √ | ' ' | 解析状态,枚举: A :解析成功 B :解析异常 |
| 12 | fduration | 耗时（毫秒） | int8 | 64 |  | √ | 0 | 耗时（毫秒） |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_parselog |  | fid |
| 2 | idx_barcm_parselog_time |  | forgid,fstarttime,fendtime |

---

## 单据体-子表 t_barcm_parselogentry

- **表名称：** 单据体-子表
- **表名：** t_barcm_parselogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 说明信息 | varchar | 512 |  | √ | ' ' | 说明信息 |
| 3 | fbarcoderuleid | 条码规则 | int8 | 64 |  | √ | 0 | [条码规则 barcm_barcoderule](../barcm_files/barcm_barcoderule.md) |
| 4 | fbarcodevalue | 条码值 | varchar | 255 |  | √ | ' ' | 条码值 |
| 5 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :成功 B :失败 |
| 6 | fentryduration | 耗时（毫秒） | int8 | 64 |  | √ | 0 | 耗时（毫秒） |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentrystarttime | 解析开始时间 | timestamp | 0 |  |  | null | 解析开始时间 |
| 9 | fentryendtime | 解析结束时间 | timestamp | 0 |  |  | null | 解析结束时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fresultvalue | 解析值 | varchar | 255 |  |  | null | 解析值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_parselogentry_fid |  | fid |
| 2 | pk_barcm_parselogentry |  | fentryid |

---

## 单据体-多语言表 t_barcm_parselogentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_barcm_parselogentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmessage | 说明信息 | varchar | 512 |  | √ | ' ' | 说明信息 |
| 2 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_parselogentry_l |  | fpkid |
| 2 | idx_barcm_plogentry_l_locale |  | fentryid,flocaleid |

---

## 条码解析日志-多语言表 t_barcm_parselog_l

- **表名称：** 条码解析日志-多语言表
- **表名：** t_barcm_parselog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述信息 | varchar | 512 |  | √ | ' ' | 描述信息 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_parselog_l_locale |  | fid,flocaleid |
| 2 | pk_barcm_parselog_l |  | fpkid |
