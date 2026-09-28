# 忽略冻结配置-msmod_freezeignore

## 业务忽略条件-子表 t_msmod_freeze_iggentry

- **表名称：** 业务忽略条件-子表
- **表名：** t_msmod_freeze_iggentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fcondition | 过滤设置 | varchar | 255 |  | √ | ' ' | 过滤设置 |
| 4 | fconditionjson | 条件json | varchar | 255 |  | √ | ' ' | 条件json |
| 5 | fconditionjson_tag | 条件json_详情 | text | 0 |  |  | null | 条件json_详情 |
| 6 | fconditionformula_tag | 条件表达式_详情 | text | 0 |  |  | null | 条件表达式_详情 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fconditionformula | 条件表达式 | varchar | 255 |  | √ | ' ' | 条件表达式 |
| 9 | fbizentityid | 业务单据 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fentryenable | 启用状态 | bpchar | 1 |  | √ | ' ' | 启用状态 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_freeze_iggentry |  | fentryid |
| 2 | idx_msmod_freeze_iggentry_fid |  | fid |

---

## 忽略冻结配置-多语言表 t_msmod_freezeignore_l

- **表名称：** 忽略冻结配置-多语言表
- **表名：** t_msmod_freezeignore_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 50 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_freezeignore_l |  | fpkid |
| 2 | idx_msmod_freezeignore_l_fid |  | fid,flocaleid |

---

## 忽略冻结配置-主表 t_msmod_freezeignore

- **表名称：** 忽略冻结配置-主表
- **表名：** t_msmod_freezeignore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fissysinit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fproviderentityid | 供应实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ffreezeentityid | 冻结单据 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_freezeignore |  | fid |
| 2 | idx_msmod_freezeignore_num |  | fnumber |
