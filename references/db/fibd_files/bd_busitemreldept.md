# 业务类型关联部门-bd_busitemreldept

## 业务类型关联部门-主表 t_bd_businessitemreldept

- **表名称：** 业务类型关联部门-主表
- **表名：** t_bd_businessitemreldept

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | frelorgid | 关联部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 报账业务类型 bd_businessitem |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_businessitemreldept_pkey |  | fid |
| 2 | idx_bdbus_bird_fbiforg |  | fbusinesstypeid,frelorgid |

---

## 业务类型关联部门-多语言表 t_bd_businessitemreldept_l

- **表名称：** 业务类型关联部门-多语言表
- **表名：** t_bd_businessitemreldept_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_businessitemreldept_l_pkey |  | fpkid |
| 2 | idx_bdbus_birdl_fidfloc |  | flocaleid,fid |
