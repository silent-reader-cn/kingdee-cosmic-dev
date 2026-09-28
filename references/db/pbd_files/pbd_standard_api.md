# 接口映射方案-pbd_standard_api

## 接口输入字段映射-子表 t_pbd_api_inputsentity

- **表名称：** 接口输入字段映射-子表
- **表名：** t_pbd_api_inputsentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fthirdfieldid | 第三方字段标识 | varchar | 80 |  | √ | ' ' | 第三方字段标识 |
| 3 | fthirdfieldtype | 第三方字段类型 | varchar | 50 |  | √ | ' ' | 第三方字段类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :是/否 ENUM :枚举 STRUCT :结构 |
| 4 | fthirdfieldname | 第三方字段名称 | varchar | 255 |  | √ | ' ' | 第三方字段名称 |
| 5 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :是/否 ENUM :枚举 STRUCT :结构 basedatafield :基础资料 |
| 6 | ffieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | ffieldid | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |
| 11 | fentryentityid | 关联第三方接口Id | int8 | 64 |  | √ | 0 | 关联第三方接口Id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_api_inputsentity |  | fentryid |
| 2 | idx_pbd_api_inputs_fid_fseq |  | fid,fseq |

---

## 接口输出字段映射-子表 t_pbd_api_outputsentity

- **表名称：** 接口输出字段映射-子表
- **表名：** t_pbd_api_outputsentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fthirdfieldid | 第三方字段标识 | varchar | 80 |  | √ | ' ' | 第三方字段标识 |
| 3 | fthirdfieldtype | 第三方字段类型 | varchar | 50 |  | √ | ' ' | 第三方字段类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :是/否 ENUM :枚举 STRUCT :结构 |
| 4 | fthirdfieldname | 第三方字段名称 | varchar | 255 |  | √ | ' ' | 第三方字段名称 |
| 5 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :是/否 ENUM :枚举 STRUCT :结构 basedatafield :基础资料 |
| 6 | ffieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | ffieldid | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |
| 11 | fentryentityid | 关联第三方接口Id | int8 | 64 |  | √ | 0 | 关联第三方接口Id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_api_outputs_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_api_outputsentity |  | fentryid |

---

## 关联第三方接口-子表 t_pbd_api_standard_entity

- **表名称：** 关联第三方接口-子表
- **表名：** t_pbd_api_standard_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplatformapi | 来源接口名称 | int8 | 64 |  | √ | 0 | [外部系统API pbd_extsys_api](../pbd_files/pbd_extsys_api.md) |
| 3 | fplatform | fplatform | int8 | 64 |  | √ | 0 |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_api_standard_entity |  | fentryid |
| 2 | idx_pbd_api_st_entity_fid_fseq |  | fid,fseq |

---

## 接口映射方案-主表 t_pbd_api_standard

- **表名称：** 接口映射方案-主表
- **表名：** t_pbd_api_standard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 接口描述 | varchar | 1000 |  | √ | ' ' | 接口描述 |
| 3 | fgroupid | 标准接口分类 | int8 | 64 |  | √ | 0 | [接口分类 pbd_api_type](../pbd_files/pbd_api_type.md) |
| 4 | fname | 标准接口名称 | varchar | 100 |  | √ | ' ' | 标准接口名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fispreinsdata | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsource | 标准接口数据源 | int8 | 64 |  | √ | 0 | [标准接口 pbd_struct](../pbd_files/pbd_struct.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_api_standard_fnumber |  | fnumber |
| 2 | pk_pbd_api_standard |  | fid |
| 3 | idx_pbd_api_standard_fmasterid |  | fmasterid |

---

## 接口映射方案-多语言表 t_pbd_api_standard_l

- **表名称：** 接口映射方案-多语言表
- **表名：** t_pbd_api_standard_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 标准接口名称 | varchar | 100 |  | √ | ' ' | 标准接口名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_api_standard_l_fid |  | fid |
| 2 | pk_pbd_api_standard_l |  | fpkid |
