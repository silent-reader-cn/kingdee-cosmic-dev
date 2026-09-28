# 单位转换关系-sco_unittransform

## 单据体-子表 t_sco_unittransformentry

- **表名称：** 单据体-子表
- **表名：** t_sco_unittransformentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenumvalue | 枚举字段值 | varchar | 255 |  | √ | ' ' | 枚举字段值,枚举: |
| 3 | fenumname | 枚举字段 | varchar | 255 |  | √ | ' ' | 枚举字段 |
| 4 | ftransrate | 转换率 | numeric | 23 | 10 | √ | 0 | 转换率 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbdunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | ftargetrate | 目标比例 | int8 | 64 |  | √ | 0 | 目标比例 |
| 8 | fsourcerate | 源比例 | int8 | 64 |  | √ | 0 | 源比例 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | ftransunit | 转换单位 | varchar | 30 |  | √ | ' ' | 转换单位,枚举: 1 :小时 2 :分钟 3 :秒 |
| 11 | fenumfield | 枚举字段标识 | varchar | 255 |  | √ | ' ' | 枚举字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_unittransformentry |  | fentryid |
| 2 | idx_sco_unittransformentry |  | fid |

---

## 单位转换关系-多语言表 t_sco_unittransform_l

- **表名称：** 单位转换关系-多语言表
- **表名：** t_sco_unittransform_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_unittransform_l |  | fpkid |
| 2 | idx_sco_unittransform_l |  | fid,flocaleid |

---

## 单位转换关系-主表 t_sco_unittransform

- **表名称：** 单位转换关系-主表
- **表名：** t_sco_unittransform

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fenumform | 枚举表单 | varchar | 255 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 11 | ftransformtype | 转换类型 | varchar | 255 |  | √ | ' ' | 转换类型,枚举: bdunit :计量单位 enum :枚举 |
| 12 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_unittransform |  | fenumform |
| 2 | pk_sco_unittransform |  | fid |
