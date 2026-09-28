# 测试计划实体-wf_testingplan

## 测试计划实体-多语言表 t_wf_testingplan_l

- **表名称：** 测试计划实体-多语言表
- **表名：** t_wf_testingplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fschemename | 配置方案名称 | varchar | 100 |  | √ | ' ' | 配置方案名称 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fstartername | 发起人姓名 | varchar | 100 |  | √ | ' ' | 发起人姓名 |
| 5 | fentityname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fdescription | 场景描述 | varchar | 2000 |  | √ | ' ' | 场景描述 |
| 8 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_testingplan_l_pkey |  | fpkid |
| 2 | idx_wf_testingplan_l_fid |  | fid |

---

## 测试计划实体-主表 t_wf_testingplan

- **表名称：** 测试计划实体-主表
- **表名：** t_wf_testingplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbilljson | 单据json | text | 0 |  |  | null | 单据json |
| 3 | fexpectedgraph | 期望运行结果图XML | text | 0 |  |  | null | 期望运行结果图XML |
| 4 | fschemeid | 配置方案ID | int8 | 64 |  | √ | 0 | 配置方案ID |
| 5 | fcaseid | 案例ID | int8 | 64 |  | √ | 0 | 案例ID |
| 6 | fentitynumber | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 7 | fstartername | fstartername | varchar | 100 |  | √ | ' ' |  |
| 8 | fentityname | fentityname | varchar | 255 |  | √ | ' ' |  |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fpath | 路径 | text | 0 |  |  | null | 路径 |
| 13 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ferrorinfo | 错误信息 | text | 0 |  |  | null | 错误信息 |
| 16 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 17 | fresultinfo | 结果信息 | text | 0 |  |  | null | 结果信息 |
| 18 | fnewbusinesskey | 新单据ID | varchar | 100 |  | √ | ' ' | 新单据ID |
| 19 | fstarterid | 发起人ID | int8 | 64 |  | √ | 0 | 发起人ID |
| 20 | fdescription | 场景描述 | varchar | 2000 |  | √ | ' ' | 场景描述 |
| 21 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 22 | fschemename | fschemename | varchar | 100 |  | √ | ' ' |  |
| 23 | fpassed | 已存档 | bpchar | 1 |  | √ | '0' | 已存档 |
| 24 | fstate | 运行状态 | varchar | 15 |  | √ | ' ' | 运行状态,枚举: successed :成功 failed :失败 notrunning :未运行 running :运行中 terminated :终止 |
| 25 | fautotest | 是否自动测试 | bpchar | 1 |  | √ | '0' | 是否自动测试 |
| 26 | fbusinesskey | 单据ID | varchar | 100 |  | √ | ' ' | 单据ID |
| 27 | fenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 28 | fnewschemeid | 新配置方案ID | int8 | 64 |  | √ | 0 | 新配置方案ID |
| 29 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 30 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_testingplan_pkey |  | fid |
| 2 | idx_wf_testingplan_caseid |  | fcaseid |
