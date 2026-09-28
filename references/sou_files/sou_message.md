# 消息管理-sou_message

## 消息管理-主表 t_pur_message

- **表名称：** 消息管理-主表
- **表名：** t_pur_message

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fbillstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :未读 B :已读 |
| 4 | freceivedate | 接收时间 | timestamp | 0 |  |  | null | 接收时间 |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | freceiverid | 接收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fimportant | 重要性 | bpchar | 1 |  | √ | ' ' | 重要性,枚举: 1 :非常重要 2 :重要 3 :一般 |
| 8 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 9 | fsenderid | 发送人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | ftitle | ftitle | varchar | 255 |  | √ | ' ' |  |
| 11 | fbiztype | 消息类型 | bpchar | 1 |  | √ | ' ' | 消息类型,枚举: 1 :询价消息 2 :招标消息 3 :竞价消息 4 :比价消息 5 :中标消息 6 :招募消息 7 :订单消息 8 :系统消息 |
| 12 | fsenddate | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 13 | fbillno | 消息编号 | varchar | 80 |  | √ | ' ' | 消息编号 |
| 14 | furgent | 紧急度 | bpchar | 1 |  | √ | ' ' | 紧急度,枚举: 1 :非常紧急 2 :紧急 3 :一般 |
| 15 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_message_pkey |  | fid |
| 2 | idx_pur_message_fsenddate |  | fsenddate |
| 3 | idx_pur_message_fbillno |  | fbillno |

---

## 消息管理-多语言表 t_pur_message_l

- **表名称：** 消息管理-多语言表
- **表名：** t_pur_message_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | ftitle | varchar | 255 |  | √ | ' ' |  |
| 3 | fremark | 消息内容 | varchar | 255 |  | √ | ' ' | 消息内容 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_message_l_pkey |  | fpkid |
| 2 | idx_pur_message_l_fid |  | fid,flocaleid |
