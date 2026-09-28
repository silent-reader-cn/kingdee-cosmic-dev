# 历史用量运算日志-mds_hisusecalclog

## 历史用量运算日志-主表 t_mds_hisusecalclog

- **表名称：** 历史用量运算日志-主表
- **表名：** t_mds_hisusecalclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcalstatus | 计算状态 | varchar | 5 |  | √ | ' ' | 计算状态,枚举: A :待运算 B :运算中 C :完成 D :终止 E :错误 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fdatafetchset | 历史取数方案 | int8 | 64 |  | √ | 0 | 取数方案定义 mds_datafetchset |
| 6 | fhisuseset | 历史用量运算方案编码 | int8 | 64 |  | √ | 0 | 历史用量运算方案定义 mds_hisuseset |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ferrmsg_tag | 详细信息_详情 | text | 0 |  |  | null | 详细信息_详情 |
| 9 | fistransform | 物料转换 | bpchar | 1 |  | √ | '0' | 物料转换 |
| 10 | fstarttime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsumtime | 计算总时长（秒） | numeric | 23 | 10 | √ | 0 | 计算总时长（秒） |
| 15 | ferrmsg | 详细信息 | varchar | 255 |  | √ | ' ' | 详细信息 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | flatest | 最新版本 | bpchar | 1 |  | √ | '0' | 最新版本 |
| 19 | fnumber | 运算号 | varchar | 80 |  | √ | ' ' | 运算号 |
| 20 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 21 | fcount | 编码总数 | int8 | 64 |  | √ | 0 | 编码总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_hisusecalclog_no |  | fnumber |
| 2 | pk_mds_hisusecalclog |  | fid |

---

## 历史用量运算日志-多语言表 t_mds_hisusecalclog_l

- **表名称：** 历史用量运算日志-多语言表
- **表名：** t_mds_hisusecalclog_l

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
| 1 | idx_mds_hisusecalclog_l_id |  | fid,flocaleid |
| 2 | pk_mds_hisusecalclog_l |  | fpkid |
