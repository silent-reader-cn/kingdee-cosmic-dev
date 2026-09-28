# 新增数据空间-ysq_rpa_queues

## 新增数据空间-多语言表 tk_ysq_rpa_queues_l

- **表名称：** 新增数据空间-多语言表
- **表名：** tk_ysq_rpa_queues_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fk_ysq_queue_desc | 数据空间描述 | varchar | 256 |  | √ | ' ' | 数据空间描述 |
| 5 | fk_ysq_queue_name | 数据空间名 | varchar | 128 |  | √ | ' ' | 数据空间名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__ysq_rpa_queues_l_0 |  | fid,flocaleid |
| 2 | pk_tk_ysq_rpa_queues_l |  | fpkid |

---

## 新增数据空间-主表 tk_ysq_rpa_queues

- **表名称：** 新增数据空间-主表
- **表名：** tk_ysq_rpa_queues

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fk_ysq_robots_no | 机器人编号 | varchar | 256 |  | √ | ' ' | 机器人编号 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fk_ysq_fail_try_times | 失败重试次数 | int8 | 64 |  |  | null | 失败重试次数 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fk_ysq_time_out | 超时时间，单位分钟 | text | 0 |  |  | null | 超时时间，单位分钟 |
| 10 | fk_ysq_queue_desc | 数据空间描述 | varchar | 256 |  | √ | ' ' | 数据空间描述 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fk_ysq_queue_name | 数据空间名 | varchar | 128 |  | √ | ' ' | 数据空间名 |
| 13 | fk_ysq_agent_alias_tag | 机器人别名_详情 | text | 0 |  |  | null | 机器人别名_详情 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fk_ysq_queue_max_items | 数据项最大数 | int8 | 64 |  |  | null | 数据项最大数 |
| 16 | fk_ysq_robots_no_tag | 机器人编号_详情 | text | 0 |  |  | null | 机器人编号_详情 |
| 17 | fk_ysq_robots_no_sel | 机器人下拉列表 | varchar | 2000 |  |  | NULL | 机器人下拉列表,枚举: |
| 18 | fk_ysq_agent_alias | 机器人别名 | varchar | 256 |  |  | NULL | 机器人别名 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_queues |  | fid |
