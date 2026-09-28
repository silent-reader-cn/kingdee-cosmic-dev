# 期限类别码表-fbd_termcategorycode

## 期限类别码表-多语言表 t_fbd_termcategorycode_l

- **表名称：** 期限类别码表-多语言表
- **表名：** t_fbd_termcategorycode_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 显示名称 | varchar | 80 |  | √ | ' ' | 显示名称 |
| 3 | flocleid | flocleid | varchar | 10 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 255 |  |  | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fbd_termcategorycode_l_pkey |  | fpkid |
| 2 | inx_fbdtermcatel_locleid |  | flocleid |

---

## 期限类别码表-主表 t_fbd_termcategorycode

- **表名称：** 期限类别码表-主表
- **表名：** t_fbd_termcategorycode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fname | 显示名称 | varchar | 80 |  | √ | ' ' | 显示名称 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fdepositnature | 适用存款性质 | varchar | 30 |  | √ | ' ' | 适用存款性质 |
| 10 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 代码 | varchar | 30 |  | √ | ' ' | 代码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fbd_termcategorycode_pkey |  | fid |
| 2 | inx_fbdtermcate_depos |  | fdepositnature |
