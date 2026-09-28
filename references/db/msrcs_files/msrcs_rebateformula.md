# 返利计算公式-msrcs_rebateformula

## 返利计算公式-多语言表 t_msrcs_rebateformula_l

- **表名称：** 返利计算公式-多语言表
- **表名：** t_msrcs_rebateformula_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebateformula_l |  | fpkid |
| 2 | idx_msrcs_rebateformulal_flid |  | fid,flocaleid |

---

## 插件变量-子表 t_msrcs_rebateformulae

- **表名称：** 插件变量-子表
- **表名：** t_msrcs_rebateformulae

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fvarname | 变量名 | varchar | 50 |  | √ | ' ' | 变量名 |
| 4 | fdescription | 变量说明 | varchar | 255 |  | √ | ' ' | 变量说明 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebateformulae |  | fentryid |
| 2 | idx_msrcs_rebateformulae_id |  | fid |

---

## 返利计算公式-主表 t_msrcs_rebateformula

- **表名称：** 返利计算公式-主表
- **表名：** t_msrcs_rebateformula

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | formulatype | 公式类型 | bpchar | 1 |  | √ | 'A' | 公式类型,枚举: A :判断公式 B :计算公式 |
| 5 | fcomment | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fmidlevelexp | 中间档实际表达式 | varchar | 2000 |  | √ | ' ' | 中间档实际表达式 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fisuniversal | 通用公式 | bpchar | 1 |  | √ | '0' | 通用公式 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fmaxlevelexp | 最高档实际表达式 | varchar | 2000 |  | √ | ' ' | 最高档实际表达式 |
| 15 | fcalcmode | 计算方式 | bpchar | 1 |  | √ | 'A' | 计算方式,枚举: A :全额累进 B :超额累进 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fenablepercent | 百分比转换 | bpchar | 1 |  | √ | '0' | 百分比转换 |
| 20 | frebateschema | 计算方案 | int8 | 64 |  | √ | 0 | [返利计算方案 msrcs_rebateschema](../msrcs_files/msrcs_rebateschema.md) |
| 21 | fformulaexp | 公式表达式 | varchar | 2000 |  | √ | ' ' | 公式表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebateformula_num |  | fnumber |
| 2 | pk_msrcs_rebateformula |  | fid |
