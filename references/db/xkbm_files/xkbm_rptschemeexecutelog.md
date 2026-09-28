# 报表自动创建方案日志-xkbm_rptschemeexecutelog

## 报表自动创建方案日志-多语言表 t_xkbm_rptschemelog_l

- **表名称：** 报表自动创建方案日志-多语言表
- **表名：** t_xkbm_rptschemelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_rptschemelog_l |  | fpkid |
| 2 | idx_xkbm_rptschemelog_l |  | fid,flocaleid |

---

## 单据体-子表 t_xkbm_rptschemelogentry

- **表名称：** 单据体-子表
- **表名：** t_xkbm_rptschemelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgenstatus | 生成状态 | varchar | 10 |  | √ | ' ' | 生成状态,枚举: 10 :成功 20 :失败 |
| 3 | frptnumber | 报表编码 | varchar | 30 |  | √ | ' ' | 报表编码 |
| 4 | fsamplenumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 5 | fsamplename | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ffailmsg | 执行结果 | varchar | 2000 |  | √ | ' ' | 执行结果 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rptschlogentry |  | fid |
| 2 | pk_t_xkbm_rptschemelogentry |  | fentryid |

---

## 报表自动创建方案日志-主表 t_xkbm_rptschemelog

- **表名称：** 报表自动创建方案日志-主表
- **表名：** t_xkbm_rptschemelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fschemeid | 方案id | int8 | 64 |  | √ | 0 | 方案id |
| 6 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | ffailcount | 失败个数 | int4 | 32 |  | √ | 0 | 失败个数 |
| 10 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | funexecutecount | 未执行个数 | int4 | 32 |  | √ | 0 | 未执行个数 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 16 | ftotalcount | 报表总数 | int4 | 32 |  | √ | 0 | 报表总数 |
| 17 | fexecutetype | 执行方式 | varchar | 10 |  | √ | ' ' | 执行方式,枚举: 10 :手动 20 :自动执行 |
| 18 | fsuccesscount | 成功个数 | int4 | 32 |  | √ | 0 | 成功个数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_rptschemelog |  | fid |
| 2 | idx_xkbm_rptschemelog |  | fnumber |
