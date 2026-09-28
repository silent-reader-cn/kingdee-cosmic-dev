# 同步参数设置-fsa_syncparam

## 维度分录-子表 t_fsa_dsyncparamdiment

- **表名称：** 维度分录-子表
- **表名：** t_fsa_dsyncparamdiment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimnumber | 维度编码 | varchar | 50 |  | √ | ' ' | 维度编码 |
| 3 | floadcompetemember | 是否自动补齐 | bpchar | 1 |  | √ | '0' | 是否自动补齐 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffiltermode | 过滤模式 | bpchar | 1 |  | √ | ' ' | 过滤模式,枚举: 1 :预置模式 2 :每次必填 3 :固定条件 |
| 6 | fdimname | 维度名称 | varchar | 50 |  | √ | ' ' | 维度名称 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | folddimnumber | 原始维度编码 | varchar | 50 |  | √ | ' ' | 原始维度编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_dsyncparamdiment |  | fdimnumber |
| 2 | pk_t_fsa_dsyncparamdiment |  | fentryid |

---

## 维度过滤条件子分录-子表 t_fsa_dsyncparamdimmement

- **表名称：** 维度过滤条件子分录-子表
- **表名：** t_fsa_dsyncparamdimmement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmembername | 成员名称 | varchar | 255 |  | √ | ' ' | 成员名称 |
| 2 | fmemberid | 成员ID | int8 | 64 |  | √ | 0 | 成员ID |
| 3 | fmemberlongnumber | 成员长编码 | varchar | 200 |  | √ | ' ' | 成员长编码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmembernumber | 成员编码 | varchar | 500 |  | √ | ' ' | 成员编码 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_dsyncparamdimmement |  | fdetailid |
| 2 | idx_fsa_dsyncparamdimmement |  | fmembernumber |

---

## 同步参数设置-多语言表 t_fsa_dsyncparam_l

- **表名称：** 同步参数设置-多语言表
- **表名：** t_fsa_dsyncparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_dsyncparam_l |  | fpkid |
| 2 | idx_fsa_dsyncparam_l |  | fid,flocaleid |

---

## 同步参数设置-主表 t_fsa_dsyncparam

- **表名称：** 同步参数设置-主表
- **表名：** t_fsa_dsyncparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fignoredimnull | 忽略为空度量值 | bpchar | 1 |  | √ | ' ' | 忽略为空度量值 |
| 5 | fdatasrctype | 数据源类型 | varchar | 50 |  | √ | ' ' | 数据源类型,枚举: 0 :自定义 bcmParamSource :星瀚合并报表 2 :星瀚预算 3 :星瀚总账 fileParamSource :导入离线数据 |
| 6 | fdescription | 描述信息 | varchar | 255 |  | √ | ' ' | 描述信息 |
| 7 | fautocomplete | 允许自动数据补齐 | bpchar | 1 |  | √ | '0' | 允许自动数据补齐 |
| 8 | ftablenumber | 数据表编码 | varchar | 30 |  | √ | ' ' | 数据表编码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | ftablename | 数据表名称 | varchar | 30 |  | √ | ' ' | 数据表名称 |
| 16 | fdatacollectionid | 数据集合 | int8 | 64 |  | √ | 0 | 数据集合 fsa_data_collection |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_syncparam_2 |  | ftablenumber,fdatacollectionid |
| 2 | pk_t_fsa_dsyncparam |  | fid |
| 3 | idx_fsa_syncparam_1 |  | fenable,fdatasrctype,fnumber |
