# 许可扣减日志-recru_certlog

## 许可扣减日志-多语言表 t_recru_certlog_l

- **表名称：** 许可扣减日志-多语言表
- **表名：** t_recru_certlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_certlog_l |  | fid,flocaleid |
| 2 | pk_recru_certlog_l |  | fpkid |

---

## 许可扣减日志-主表 t_recru_certlog

- **表名称：** 许可扣减日志-主表
- **表名：** t_recru_certlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ffailmsg | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcertstatus | 许可扣减状态 | varchar | 10 |  | √ | ' ' | 许可扣减状态,枚举: 1 :成功 0 :失败 |
| 8 | ffailmsg_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 9 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | varchar | 50 |  | √ | ' ' | 主数据内码 |
| 12 | fsession | 会话 | varchar | 50 |  | √ | ' ' | 会话 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fquata | 扣减数量 | int4 | 32 |  | √ | 0 | 扣减数量 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_certlog_operate |  | fcreatorid |
| 2 | pk_recru_certlog |  | fid |
| 3 | idx_recru_certlog_session |  | fsession |
