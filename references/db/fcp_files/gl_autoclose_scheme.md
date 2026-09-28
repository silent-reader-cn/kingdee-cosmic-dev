# 自动结账方案-gl_autoclose_scheme

## 自动结账方案-主表 t_gl_autoclose_scheme

- **表名称：** 自动结账方案-主表
- **表名：** t_gl_autoclose_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbizsystems | 业务系统 | varchar | 50 |  | √ | ' ' | 业务系统,枚举: fa :固定资产 gl :总账 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 8 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 9 | fcreatime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fmodifytime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_autoclose_scheme_num |  | fnumber |
| 2 | pk_gl_autoclose_scheme |  | fid |

---

## 自动结账方案-多语言表 t_gl_autoclose_scheme_l

- **表名称：** 自动结账方案-多语言表
- **表名：** t_gl_autoclose_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 801 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 200 |  | √ | ' ' | 方案名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_autoclose_scheme_l |  | fpkid |
| 2 | idx_autoclose_sch_flid |  | fid,flocaleid |

---

## 执行操作详情-子表 t_gl_autoclose_opdetail

- **表名称：** 执行操作详情-子表
- **表名：** t_gl_autoclose_opdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foperateconfig | 执行操作 | varchar | 3 |  | √ | '' | 执行操作 |
| 2 | fexecuteseq | 执行顺序 | int4 | 32 |  | √ | 0 | 执行顺序 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fexecplanids | 执行方案id列表 | varchar | 1000 |  | √ | ' ' | 执行方案id列表 |
| 6 | foperation | 业务操作 | varchar | 50 |  | √ | ' ' | 业务操作,枚举: |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_autoclose_opdetail |  | fdetailid |
| 2 | idx_autoclose_op_eid |  | fentryid |

---

## 账簿-多选基础资料表 t_gl_autoclose_ref_book

- **表名称：** 账簿-多选基础资料表
- **表名：** t_gl_autoclose_ref_book

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_autoclose_ref_book |  | fpkid |
| 2 | idx_autoclose_ref_book_id |  | fid |

---

## 执行规则-子表 t_gl_autoclose_rule

- **表名称：** 执行规则-子表
- **表名：** t_gl_autoclose_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fscheduleplanid | 调度计划id | varchar | 18 |  | √ | ' ' | 调度计划id |
| 4 | fbizsystem | 业务系统 | varchar | 50 |  | √ | ' ' | 业务系统 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_autoclose_rule |  | fentryid |
| 2 | idx_gl_autoclose_rule_fid |  | fid |
