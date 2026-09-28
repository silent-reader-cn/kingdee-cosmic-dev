# 出差用车制度-er_trip_carregulation

## 出差用车制度-多语言表 t_er_trip_carregulation_l

- **表名称：** 出差用车制度-多语言表
- **表名：** t_er_trip_carregulation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 制度名称 | varchar | 100 |  | √ | ' ' | 制度名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_trip_carregulation_l |  | fpkid |
| 2 | idx_trip_carregulation_l_id |  | fid,flocaleid |

---

## 出差用车制度-主表 t_er_trip_carregulation

- **表名称：** 出差用车制度-主表
- **表名：** t_er_trip_carregulation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fscenetype | 因公出行场景 | varchar | 30 |  | √ | ' ' | 因公出行场景,枚举: 0 :个人用车 1 :商务出行 2 :差旅 3 :加班 4 :办公地点通勤 91 :代叫车 92 :接送机 96 :行前审批 8 :企业班车 |
| 5 | fisapprove | 制度需要审批 | bpchar | 1 |  | √ | '0' | 制度需要审批 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fserver | 服务商 | int8 | 64 |  | √ | 0 | [服务商设置 er_biz_info](../em_files/er_biz_info.md) |
| 11 | fenable | 制度状态 | varchar | 30 |  | √ | ' ' | 制度状态,枚举: 0 :停用 1 :正常 2 :删除 3 :过期 |
| 12 | fisusequota | 使用个人限额 | bpchar | 1 |  | √ | '0' | 使用个人限额 |
| 13 | fnumber | 制度编号 | varchar | 200 |  | √ | ' ' | 制度编号 |
| 14 | fapprovaltype | 审批类型 | varchar | 10 |  | √ | ' ' | 审批类型,枚举: 0 :无需审批 1 :差旅 2 :行前审批按次数 3 :行前审批按日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_trip_carregulatio_num |  | fnumber |
| 2 | pk_t_er_trip_carregulation |  | fid |
