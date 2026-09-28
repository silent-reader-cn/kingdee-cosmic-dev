# 云之家待办-msg_yzjtodo

## 云之家待办-主表 t_wf_yzjtodo

- **表名称：** 云之家待办-主表
- **表名：** t_wf_yzjtodo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateurl | 待办创建地址 | varchar | 100 |  | √ | ' ' | 待办创建地址 |
| 3 | fappsecret | 轻应用秘钥 | varchar | 100 |  | √ | ' ' | 轻应用秘钥 |
| 4 | fmsgresult | 任务结果 | bpchar | 1 |  | √ | '0' | 任务结果 |
| 5 | fmsgstate | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态 |
| 6 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 7 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 8 | fauthurl | 云之家访问地址 | varchar | 100 |  | √ | ' ' | 云之家访问地址 |
| 9 | fappid | 轻应用ID | varchar | 100 |  | √ | ' ' | 轻应用ID |
| 10 | fretries | 检测重试次数 | int8 | 64 |  | √ | 0 | 检测重试次数 |
| 11 | fusername | fusername | varchar | 100 |  | √ | ' ' |  |
| 12 | fcheckurl | 待办检测地址 | varchar | 100 |  | √ | ' ' | 待办检测地址 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: yunzhijia :云之家 yunzhijiaeco :生态云之家 |
| 15 | fopenid | 云之家人员ID | varchar | 100 |  | √ | ' ' | 云之家人员ID |
| 16 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | feid | 主体工作圈ID | int8 | 64 |  | √ | 0 | 主体工作圈ID |
| 18 | fdealurl | 待办处理地址 | varchar | 100 |  | √ | ' ' | 待办处理地址 |
| 19 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 20 | fecosecret | 生态圈秘钥 | varchar | 200 |  | √ | ' ' | 生态圈秘钥 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_yzjtodo_taskid |  | ftaskid |
| 2 | t_wf_yzjtodo_pkey |  | fid |
| 3 | idx_wf_yzjtodo_procinstid |  | fprocinstid |

---

## 云之家待办-多语言表 t_wf_yzjtodo_l

- **表名称：** 云之家待办-多语言表
- **表名：** t_wf_yzjtodo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusername | 用户名 | varchar | 100 |  | √ | ' ' | 用户名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_yzjtodo_l_pkey |  | fpkid |
| 2 | idx_wf_yzjtodo_l |  | fid,flocaleid |
