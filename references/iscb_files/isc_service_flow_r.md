# 服务流程（已发布）-isc_service_flow_r

## 服务流程（已发布）-主表 t_isc_service_flow_r

- **表名称：** 服务流程（已发布）-主表
- **表名：** t_isc_service_flow_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 4 | finit_mode | 启动方式 | varchar | 30 |  | √ | ' ' | 启动方式,枚举: MANUAL :人工启动 TIMER :定时启动 EVENT :事件触发 MESSAGE :消息启动 |
| 5 | fdefine_json | 流程定义 | varchar | 255 |  | √ | ' ' | 流程定义 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 发布人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fflow_id | 服务流程ID | int8 | 64 |  | √ | 0 | 服务流程ID |
| 11 | fdefine_json_tag | 流程定义_详情 | text | 0 |  |  | null | 流程定义_详情 |
| 12 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 14 | fversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_service_flow_r_c |  | fcreatetime |
| 2 | idx_isc_service_flow_r_n |  | fnumber |
| 3 | idx_isc_service_flow_r_f_id |  | fflow_id,fversion |
| 4 | t_isc_service_flow_r_pkey |  | fid |

---

## 服务流程（已发布）-多语言表 t_isc_service_flow_r_l

- **表名称：** 服务流程（已发布）-多语言表
- **表名：** t_isc_service_flow_r_l

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
| 1 | idx_isc_service_flow_r_l_i |  | fid,flocaleid |
| 2 | t_isc_service_flow_r_l_pkey |  | fpkid |
