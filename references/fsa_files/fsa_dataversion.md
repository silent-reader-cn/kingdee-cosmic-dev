# 数据版本-fsa_dataversion

## 过滤成员-子表 t_fsa_dv_filtermembers

- **表名称：** 过滤成员-子表
- **表名：** t_fsa_dv_filtermembers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmembername | 过滤成员名称 | varchar | 500 |  | √ | ' ' | 过滤成员名称 |
| 2 | fmemberid | 过滤成员ID | int8 | 64 |  | √ | 0 | 过滤成员ID |
| 3 | fmemberlongnumber | 过滤成员长编码 | varchar | 200 |  | √ | ' ' | 过滤成员长编码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmembernumber | 过滤成员编码 | varchar | 50 |  | √ | ' ' | 过滤成员编码 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_dv_filtermembers_1 |  | fentryid |
| 2 | pk_t_fsa_dv_filtermembers |  | fdetailid |

---

## 过滤字段-子表 t_fsa_dv_filterfields

- **表名称：** 过滤字段-子表
- **表名：** t_fsa_dv_filterfields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimnumber | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ffiltermode | 过滤模式 | bpchar | 1 |  | √ | ' ' | 过滤模式 |
| 5 | fdimname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | folddimnumber | 原始维度编码 | varchar | 50 |  | √ | ' ' | 原始维度编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_dv_filterfields |  | fentryid |
| 2 | idx_fsa_dv_filterfields |  | fid |

---

## 数据版本-主表 t_fsa_dataversion

- **表名称：** 数据版本-主表
- **表名：** t_fsa_dataversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | varchar | 2 |  | √ | ' ' | 状态,枚举: 0 :新增 1 :进行中 2 :可用 3 :启用 9 :失败 -1 :删除 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | frefparam | 引用参数 | int8 | 64 |  | √ | 0 | 引用参数 |
| 5 | ftargetentity | 目标实体对象编码 | varchar | 30 |  | √ | ' ' | 目标实体对象编码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 8 | fsrctype | 来源类型 | varchar | 2 |  | √ | ' ' | 来源类型,枚举: 0 :同步参数 1 :数据指标 |
| 9 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_dataversion |  | fid |
| 2 | idx_fsa_dataversion_2 |  | fversion |
| 3 | idx_fsa_dataversion_1 |  | frefparam,fversion |
