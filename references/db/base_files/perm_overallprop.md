# 全局数据规则控制维度-perm_overallprop

## 全局数据规则控制维度-多语言表 t_perm_overallprop1_l

- **表名称：** 全局数据规则控制维度-多语言表
- **表名：** t_perm_overallprop1_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_overallprop1_l |  | fpkid |
| 2 | idx_perm_overallprop1_l_0 |  | fid,flocaleid |

---

## 全局数据规则控制维度-主表 t_perm_overallprop1

- **表名称：** 全局数据规则控制维度-主表
- **表名：** t_perm_overallprop1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | null | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fentitynum | 基础资料类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: BasedataProp :基础资料 TextProp :文本 ComboProp :下拉列表 |
| 5 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_overallprop1 |  | fid |
