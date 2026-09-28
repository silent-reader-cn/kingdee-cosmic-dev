# 数据权限-perm_dataperm

## 数据权限-多语言表 t_perm_dataperm_l

- **表名称：** 数据权限-多语言表
- **表名：** t_perm_dataperm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_dataperm_l |  | fid,flocaleid |
| 2 | t_perm_dataperm_l_pkey |  | fpkid |

---

## 数据权限-主表 t_perm_dataperm

- **表名称：** 数据权限-主表
- **表名：** t_perm_dataperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | varchar | 18 |  | √ | ' ' | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | 权限项 perm_permitem |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_dataperm_pkey |  | fid |
| 2 | idx_perm_dataperm |  | fpermitemid,fnumber |

---

## 字段规则-子表 t_perm_datapermrule

- **表名称：** 字段规则-子表
- **表名：** t_perm_datapermrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | flogicsymbol | 逻辑 | varchar | 10 |  | √ | ' ' | 逻辑,枚举: |
| 3 | fcomparesymbol | 条件 | varchar | 10 |  | √ | ' ' | 条件,枚举: |
| 4 | ffieldname | 字段 | varchar | 30 |  | √ | ' ' | 字段,枚举: |
| 5 | fcomparevalue | 值 | varchar | 50 |  | √ | ' ' | 值 |
| 6 | ffielddisplayname | ffielddisplayname | varchar | 100 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdetailid | fdetailid | varchar | 18 |  | √ | ' ' | id |
| 9 | fcomparevaluetype | fcomparevaluetype | varchar | 10 |  | √ | ' ' |  |
| 10 | fentryid | fentryid | varchar | 18 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_datapermrule_pkey |  | fdetailid |
| 2 | ix_perm_00000009 |  | fentryid |

---

## 业务对象分录-子表 t_perm_datapermentry

- **表名称：** 业务对象分录-子表
- **表名：** t_perm_datapermentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | frule | 数据规则 | text | 0 |  |  | null | 数据规则 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 5 | fentryid | fentryid | varchar | 18 |  | √ | ' ' | id |
| 6 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_datapermentry |  | fid |
| 2 | t_perm_datapermentry_pkey |  | fentryid |
