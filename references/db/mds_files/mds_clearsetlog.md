# 需求计划清空处理日志-mds_clearsetlog

## 单据体-子表 t_mds_clearsetlogentry

- **表名称：** 单据体-子表
- **表名：** t_mds_clearsetlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | ffcvrnnum | 版本 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_clearsetlogentry |  | fid,fseq |
| 2 | pk_mds_clearsetlogentry |  | fentryid |

---

## 需求计划清空处理日志-主表 t_mds_clearsetlog

- **表名称：** 需求计划清空处理日志-主表
- **表名：** t_mds_clearsetlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ferrorinfo | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | frepeat | 重复清空 | bpchar | 1 |  | √ | '0' | 重复清空 |
| 7 | fpredtime | 预约时间 | int8 | 64 |  | √ | 0 | 预约时间 |
| 8 | frunningtype | 运行时间类型 | varchar | 30 |  | √ | ' ' | 运行时间类型,枚举: 0 :立即清空 1 :预约时间清空 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 12 | fsummin | 计算总时长（秒） | numeric | 23 | 10 | √ | 0.0000000000 | 计算总时长（秒） |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsyncresult | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :成功 B :失败 |
| 16 | fstartdate | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | ferrorinfo_tag | 异常信息_详情 | varchar | 2000 |  | √ | ' ' | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mds_clearsetlog_number |  | fnumber |
| 2 | pk_mds_clearsetlog |  | fid |

---

## 需求计划清空处理日志-多语言表 t_mds_clearsetlog_l

- **表名称：** 需求计划清空处理日志-多语言表
- **表名：** t_mds_clearsetlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_clearsetlog_l |  | fpkid |
| 2 | idx_mds_clearsetlog_l |  | fid,flocaleid |
