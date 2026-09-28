# 函数配置-plm_rengine_function

## 参数-多语言表 t_plm_egn_f_params_l

- **表名称：** 参数-多语言表
- **表名：** t_plm_egn_f_params_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 导入依赖包代码分录-多语言表 t_plm_rengine_f_import_l

- **表名称：** 导入依赖包代码分录-多语言表
- **表名：** t_plm_rengine_f_import_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 函数配置-多语言表 t_plm_egn_function_l

- **表名称：** 函数配置-多语言表
- **表名：** t_plm_egn_function_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fsimplename | fsimplename | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 功能描述 | varchar | 255 |  | √ | ' ' | 功能描述 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_egn_function_l |  | fid,flocaleid |
| 2 | pk_plm_egn_function_l |  | fpkid |

---

## 导入依赖包代码分录-子表 t_plm_rengine_f_import

- **表名称：** 导入依赖包代码分录-子表
- **表名：** t_plm_rengine_f_import

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 参数-子表 t_plm_egn_f_params

- **表名称：** 参数-子表
- **表名：** t_plm_egn_f_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 函数配置-主表 t_plm_egn_function

- **表名称：** 函数配置-主表
- **表名：** t_plm_egn_function

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 函数分类 | int8 | 64 |  | √ | 0 | [公式函数分类 plm_rengine_functiontype](../plmsm_files/plm_rengine_functiontype.md) |
| 5 | ffuncexp | 函数体 | varchar | 50 |  | √ | ' ' | 函数体 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffunkey | 函数关键词 | varchar | 50 |  | √ | ' ' | 函数关键词 |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fdescription | 功能描述 | varchar | 1500 |  | √ | ' ' | 功能描述 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 2 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ffuncdatatype | 返回值类型 | varchar | 100 |  |  | ' ' | 返回值类型,枚举: String :字符串 BigDecimal :数值 Date :日期 Integer :整型 Object :对象 |
| 16 | fexample | 函数示例 | varchar | 1500 |  | √ | ' ' | 函数示例 |
| 17 | fenable | 使用状态 | varchar | 2 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | ffunsource | 函数来源 | varchar | 50 |  | √ | ' ' | 函数来源,枚举: HR :HR预置函数 Platform :平台内置函数 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | funiquecode | 唯一编码 | varchar | 50 |  | √ | ' ' | 唯一编码 |
| 21 | fdefine | 函数定义 | varchar | 100 |  | √ | ' ' | 函数定义 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_egn_function |  | fnumber |
| 2 | pk_plm_egn_function |  | fid |
