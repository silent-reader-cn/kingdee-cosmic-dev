# 案例-wf_cases

## 案例-主表 t_wf_cases

- **表名称：** 案例-主表
- **表名：** t_wf_cases

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftestpoint | 测试要点 | text | 0 |  |  | null | 测试要点 |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fkeywords | 场景关键字 | varchar | 500 |  | √ | ' ' | 场景关键字 |
| 5 | fnewprocdefid | 新流程定义ID | int8 | 64 |  | √ | 0 | 新流程定义ID |
| 6 | fflowchart | fflowchart | varchar | 500 |  | √ | ' ' |  |
| 7 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fresult | fresult | bpchar | 1 |  |  | null |  |
| 10 | fmainpoint | 流程设置要点 | text | 0 |  |  | null | 流程设置要点 |
| 11 | fschememapjson | 新旧方案ID映射 | text | 0 |  |  | null | 新旧方案ID映射 |
| 12 | fexecutemessage | fexecutemessage | text | 0 |  |  | null |  |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fprocessresource | 流程资源 | text | 0 |  |  | null | 流程资源 |
| 15 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | ffilename | ffilename | varchar | 200 |  | √ | ' ' |  |
| 17 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fscene | 场景描述 | text | 0 |  |  | null | 场景描述 |
| 19 | fmainclass | fmainclass | varchar | 200 |  | √ | ' ' |  |
| 20 | fprocesstrend | fprocesstrend | text | 0 |  |  | null |  |
| 21 | fenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 22 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_cases_fnumber |  | fnumber |
| 2 | t_wf_cases_pkey |  | fid |

---

## 案例-多语言表 t_wf_cases_l

- **表名称：** 案例-多语言表
- **表名：** t_wf_cases_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_cases_localeid |  | fid,flocaleid |
| 2 | t_wf_cases_l_pkey |  | fpkid |
