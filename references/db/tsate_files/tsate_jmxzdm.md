# 减免性质代码全集-tsate_jmxzdm

## 减免性质代码全集-主表 t_tsate_jmxzdm

- **表名称：** 减免性质代码全集-主表
- **表名：** t_tsate_jmxzdm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fjmsxdm | 减免事项代码 | varchar | 50 |  | √ | ' ' | 减免事项代码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 减免性质代码 | varchar | 50 |  | √ | ' ' | 减免性质代码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_jmxzdm |  | fid |
| 2 | idx_tsate_jmxzdm |  | fjmsxdm |

---

## 减免性质代码全集-多语言表 t_tsate_jmxzdm_l

- **表名称：** 减免性质代码全集-多语言表
- **表名：** t_tsate_jmxzdm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 减免性质名称 | varchar | 1000 |  | √ | ' ' | 减免性质名称 |
| 3 | fjmsxmc | 减免事项名称 | varchar | 1000 |  | √ | ' ' | 减免事项名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_jmxzdm_l_0 |  | fid,flocaleid |
| 2 | pk_tsate_jmxzdm_l |  | fpkid |
