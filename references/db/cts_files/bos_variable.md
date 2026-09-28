# 全局变量-bos_variable

## 全局变量-主表 t_bas_variable

- **表名称：** 全局变量-主表
- **表名：** t_bas_variable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 变量描述 | varchar | 256 |  | √ | ' ' | 变量描述 |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [变量分组 bos_variablegroup](../cts_files/bos_variablegroup.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fvariablecode | 本地变量 | varchar | 120 |  | √ | ' ' | 本地变量 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftype | 变量类型 | bpchar | 1 |  | √ | ' ' | 变量类型,枚举: 0 :单一变量 1 :合集变量 |
| 12 | fvariablerule | 变量规则 | varchar | 256 |  | √ | ' ' | 变量规则 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 变量 | varchar | 120 |  | √ | ' ' | 变量 |
| 15 | fusescene | 应用场景 | bpchar | 1 |  | √ | 'A' | 应用场景,枚举: A :脚本打印 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_variable |  | fid |
| 2 | idx_bas_variable_n |  | fnumber,fgroupid |

---

## 全局变量-多语言表 t_bas_variable_l

- **表名称：** 全局变量-多语言表
- **表名：** t_bas_variable_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 变量描述 | varchar | 256 |  | √ | ' ' | 变量描述 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_variable_l |  | fid,flocaleid |
| 2 | pk_t_bas_variable_l |  | fpkid |
