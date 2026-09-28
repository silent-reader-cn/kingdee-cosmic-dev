# 付款条件-pur_paycond

## 付款条件-多语言表 t_pur_paycond_l

- **表名称：** 付款条件-多语言表
- **表名：** t_pur_paycond_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fremark | 描述 | varchar | 255 |  |  | null | 描述 |
| 3 | fname | 名称 | varchar | 100 |  |  | null | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_paycond_l |  | fid,flocaleid |
| 2 | t_pur_paycond_l_pkey |  | fpkid |

---

## 付款条件-主表 t_pur_paycond

- **表名称：** 付款条件-主表
- **表名：** t_pur_paycond

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 业务组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | 人员 bos_user |
| 8 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 9 | fcontrolstatus | fcontrolstatus | bpchar | 1 |  |  | null |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | fenable | 使用状态 | bpchar | 1 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  |  | null | 编码 |
| 16 | fauditorid | fauditorid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_paycond_number |  | fnumber |
| 2 | t_pur_paycond_pkey |  | fid |
