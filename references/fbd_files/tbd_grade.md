# 评级档案-tbd_grade

## 评级档案-主表 t_tbd_grade

- **表名称：** 评级档案-主表
- **表名：** t_tbd_grade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fratingagencyid | 评级机构 | int8 | 64 |  | √ | 0 | 评级机构 tbd_ratingagency |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 5 | fratingscale | 评级 | varchar | 80 |  | √ | ' ' | 评级 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fratingscaleid | 选择的评级分录id | varchar | 30 |  | √ | ' ' | 选择的评级分录id |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fratingtype | 评级类型 | varchar | 30 |  | √ | ' ' | 评级类型,枚举: bd_country :国家地区 tbd_issuer :发行人 tm_bondissuef7 :债券发行 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fratingobject | 评级对象 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 15 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 16 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 17 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tbd_grade_n |  | fnumber |
| 2 | pk_t_tbd_grade |  | fid |

---

## 评级档案-多语言表 t_tbd_grade_l

- **表名称：** 评级档案-多语言表
- **表名：** t_tbd_grade_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tbd_grade_l_id |  | fid,flocaleid |
| 2 | pk_t_tbd_grade_l |  | fpkid |
