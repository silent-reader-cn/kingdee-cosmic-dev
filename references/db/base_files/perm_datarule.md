# 数据规则方案-perm_datarule

## 基础资料属性数据规则分录-子表 t_perm_datarule_prop

- **表名称：** 基础资料属性数据规则分录-子表
- **表名：** t_perm_datarule_prop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropentnum | 属性业务对象 | varchar | 36 |  |  | ' ' | 主实体对象 bos_entityobject |
| 3 | fdataruleid | 属性数据规则方案 | int8 | 64 |  | √ | 0 | 数据规则方案 perm_datarule |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropkey | 属性标识 | varchar | 60 |  | √ | ' ' | 属性标识 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_datarule_prop |  | fpropkey |
| 2 | t_perm_datarule_prop_pkey |  | fentryid |

---

## 单据体-子表 t_perm_datarule_entry

- **表名称：** 单据体-子表
- **表名：** t_perm_datarule_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fopkey | fopkey | varchar | 30 |  | √ | ' ' |  |
| 3 | foptype | foptype | varchar | 30 |  | √ | ' ' |  |
| 4 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | 权限项 perm_permitem |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdataruleid | 数据规则方案 | int8 | 64 |  | √ | 0 | 数据规则方案 perm_datarule |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_datarule_entry_pkey |  | fentryid |
| 2 | idx_perm_datarule_entry |  | fid,fpermitemid |

---

## 数据规则方案-主表 t_perm_datarule

- **表名称：** 数据规则方案-主表
- **表名：** t_perm_datarule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 4 | fentitynum | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fapplyscope | 适用范围 | bpchar | 1 |  | √ | '1' | 适用范围,枚举: 1 :业务对象 2 :应用 3 :云 4 :全局 |
| 7 | fdescription | 描述 | varchar | 500 |  |  | ' ' | 描述 |
| 8 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | frule | 规则 | text | 0 |  |  | null | 规则 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcloudid | 云 | varchar | 36 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 15 | fisdetail | 是否明细方案 | bpchar | 1 |  | √ | '1' | 是否明细方案 |
| 16 | frule_tag | frule_tag | text | 0 |  |  | null |  |
| 17 | fissystemxk | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 方案编码 | varchar | 100 |  | √ | ' ' | 方案编码 |
| 20 | fnocoderule | 无代码平台规则 | text | 0 |  |  | null | 无代码平台规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_datarule_pkey |  | fid |
| 2 | idx_perm_datarule |  | fbizappid,fentitynum |

---

## 数据规则方案-多语言表 t_perm_datarule_l

- **表名称：** 数据规则方案-多语言表
- **表名：** t_perm_datarule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_datarule_l |  | fid,flocaleid |
| 2 | t_perm_datarule_l_pkey |  | fpkid |
