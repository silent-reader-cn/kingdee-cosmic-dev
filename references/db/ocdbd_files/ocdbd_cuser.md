# 渠道用户-ocdbd_cuser

## 全渠道用户角色-多选基础资料表 t_ocdbd_curole

- **表名称：** 全渠道用户角色-多选基础资料表
- **表名：** t_ocdbd_curole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 全渠道用户角色 ocdbd_role |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_curole_fbid |  | fid,fbasedataid |
| 2 | pk_ocdbd_curole |  | fpkid |

---

## 渠道用户-主表 t_ocdbd_cuser

- **表名称：** 渠道用户-主表
- **表名：** t_ocdbd_cuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcontroltype | 管辖范围 | bpchar | 1 |  | √ | ' ' | 管辖范围,枚举: A :按行政组织管辖 B :按指定行政组织管辖 C :按指定销售组织管辖 D :按指定渠道管辖 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fuserid | 用户编码 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcashierid | 收银角色 | int8 | 64 |  | √ | 0 | 收银角色 ocdbd_cashierrole |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_cuser |  | fid |
| 2 | idx_ocdbd_cuser_userid |  | fuserid |

---

## 渠道管辖范围-子表 t_ocdbd_cuchlscope

- **表名称：** 渠道管辖范围-子表
- **表名：** t_ocdbd_cuchlscope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchanneluserid | (原)渠道用户主键 | int8 | 64 |  | √ | 0 | (原)渠道用户主键 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fchannelid | 渠道编码 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_cuchlscope |  | fentryid |
| 2 | idx_ocdbd_cuchlscope_fid |  | fid |

---

## 组织管辖范范围-子表 t_ocdbd_cuorgscope

- **表名称：** 组织管辖范范围-子表
- **表名：** t_ocdbd_cuorgscope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fisincludeallsub | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_cuorgscope_fid |  | fid |
| 2 | pk_ocdbd_cuorgscope |  | fentryid |
