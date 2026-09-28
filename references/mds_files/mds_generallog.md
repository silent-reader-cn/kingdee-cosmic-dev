# 通用备货运算日志-mds_generallog

## 通用备货运算日志-多语言表 t_mds_generallog_l

- **表名称：** 通用备货运算日志-多语言表
- **表名：** t_mds_generallog_l

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
| 1 | idx_mds_generallog_l_id |  | fid,flocaleid |
| 2 | pk_mds_generallog_l |  | fpkid |

---

## 通用备货运算日志-主表 t_mds_generallog

- **表名称：** 通用备货运算日志-主表
- **表名：** t_mds_generallog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetsumtime | 计算总时长（秒） | numeric | 23 | 10 | √ | 0 | 计算总时长（秒） |
| 3 | fspecialendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 4 | fcustomercount | 客户总数 | int8 | 64 |  | √ | 0 | 客户总数 |
| 5 | fusecountmax | 最大使用频率 | int8 | 64 |  | √ | 0 | 最大使用频率 |
| 6 | fspecialreq | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 7 | ferrmsg_tag | 详细信息_详情 | text | 0 |  |  | null | 详细信息_详情 |
| 8 | fspecialnocount | 特殊编码总数 | int8 | 64 |  | √ | 0 | 特殊编码总数 |
| 9 | fsugstarttime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 10 | factypecount | 检修设备类型总数 | int8 | 64 |  | √ | 0 | 检修设备类型总数 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fhisusecalclog | 历史用量运算日志 | int8 | 64 |  | √ | 0 | 历史用量运算日志 mds_hisusecalclog |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | ftargetstarttime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 17 | fsugendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 18 | fusecountmin | 最小使用频率 | int8 | 64 |  | √ | 0 | 最小使用频率 |
| 19 | fspecialsumtime | 计算总时长（秒） | numeric | 23 | 10 | √ | 0 | 计算总时长（秒） |
| 20 | fgeneralplan | 通用备货计划 | int8 | 64 |  | √ | 0 | 取数方案定义 mds_datafetchset |
| 21 | frepeatcal | 重运算 | bpchar | 1 |  | √ | '0' | 重运算 |
| 22 | fsugsumtime | 计算总时长（秒） | numeric | 23 | 10 | √ | 0 | 计算总时长（秒） |
| 23 | fcalstatus | 计算状态 | varchar | 5 |  | √ | ' ' | 计算状态,枚举: A :待运算 B :运算中 C :完成 D :终止 E :错误 |
| 24 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fplansumtime | 计算总时长（秒） | numeric | 23 | 10 | √ | 0 | 计算总时长（秒） |
| 27 | fchecktypecount | 检修级别总数 | int8 | 64 |  | √ | 0 | 检修级别总数 |
| 28 | fhisuseset | 历史用量运算方案 | int8 | 64 |  | √ | 0 | 历史用量运算方案定义 mds_hisuseset |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | ftargetendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 31 | fplancount | 计划总数 | int8 | 64 |  | √ | 0 | 计划总数 |
| 32 | fstarttime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 33 | fstocknocount | 备货编码总数 | int8 | 64 |  | √ | 0 | 备货编码总数 |
| 34 | fsumtime | 计算总时长（秒） | numeric | 23 | 10 | √ | 0 | 计算总时长（秒） |
| 35 | ferrmsg | 详细信息 | varchar | 255 |  | √ | ' ' | 详细信息 |
| 36 | fgeneralset | 通用备货方案 | int8 | 64 |  | √ | 0 | 通用备货方案 mds_generalset |
| 37 | fspecialstarttime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 38 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 39 | flatest | 最新版本 | bpchar | 1 |  | √ | '0' | 最新版本 |
| 40 | fplanendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 41 | fnumber | 通用备货运算号 | varchar | 80 |  | √ | ' ' | 通用备货运算号 |
| 42 | fspecialcond | 特定条件 | bpchar | 1 |  | √ | '0' | 特定条件 |
| 43 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 44 | fplanstarttime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_generallog |  | fid |
| 2 | idx_mds_generallog_number |  | fnumber |
