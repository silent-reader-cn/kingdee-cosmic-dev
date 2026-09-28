# 变更方案-bdtaxr_changemodel

## 变更方案-主表 t_bdtaxr_changemodel

- **表名称：** 变更方案-主表
- **表名：** t_bdtaxr_changemodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcustomparameter_tag | 详情 | text | 0 |  |  | null | 详情 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsrcbillid | 源单 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fareaconditionjson_tag | 数据范围条件json_详情 | text | 0 |  |  | null | 数据范围条件json_详情 |
| 8 | fvalidoptype | 校验时机 | varchar | 50 |  | √ | ' ' | 校验时机,枚举: submit :提交 audit :审核 |
| 9 | fxbillid | 变更单 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcustomparameter |  | varchar | 255 |  | √ | ' ' |  |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fareaconditionjson | 数据范围条件json | varchar | 255 |  | √ | ' ' | 数据范围条件json |
| 16 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 19 | fareaconditiondesc | 条件描述 | varchar | 2000 |  | √ | ' ' | 条件描述 |
| 20 | fpluginname | fpluginname | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_changem_num |  | fnumber |
| 2 | pk_bdtaxr_changemodel |  | fid |

---

## 校验条件实体-子表 t_bdtaxr_changemodelve

- **表名称：** 校验条件实体-子表
- **表名：** t_bdtaxr_changemodelve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdesc | 条件描述 | varchar | 50 |  | √ | ' ' | 条件描述 |
| 5 | fvalidconditionjson_tag | 反写条件json_详情 | text | 0 |  |  | null | 反写条件json_详情 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fvalidconditionjson | 反写条件json | varchar | 255 |  | √ | ' ' | 反写条件json |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_changemodelve |  | fentryid |
| 2 | idx_bdtaxr_changemve_fk |  | fid |

---

## 插件实体-子表 t_bdtaxr_changemodelpe

- **表名称：** 插件实体-子表
- **表名：** t_bdtaxr_changemodelpe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpluginenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 3 | fpluginjson | 插件JSON | varchar | 200 |  | √ | ' ' | 插件JSON |
| 4 | fclassname | 类名 | varchar | 100 |  | √ | ' ' | 类名 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fplugintype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :Java插件 1 :JSript插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_changempe_fk |  | fid |
| 2 | pk_bdtaxr_changemodelpe |  | fentryid |

---

## 字段映射-子表 t_bdtaxr_changemodelfe

- **表名称：** 字段映射-子表
- **表名：** t_bdtaxr_changemodelfe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 源单字段 | varchar | 255 |  | √ | ' ' | 源单字段 |
| 3 | fcandisplay | 可显示 | bpchar | 1 |  | √ | '0' | 可显示 |
| 4 | fclearsourcefield | 清除 | varchar | 50 |  | √ | ' ' | 清除 |
| 5 | fcanenable | 可变更 | bpchar | 1 |  | √ | '0' | 可变更 |
| 6 | ffieldformula | 计算公式 | varchar | 500 |  | √ | ' ' | 计算公式 |
| 7 | ftargetfield | 变更单字段 | varchar | 255 |  | √ | ' ' | 变更单字段 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdrawagainfilter | 追加时过滤 | bpchar | 1 |  | √ | '0' | 追加时过滤 |
| 10 | fdrawfilter | 过滤 | bpchar | 1 |  | √ | '0' | 过滤 |
| 11 | fcanwriteback | 可反写 | bpchar | 1 |  | √ | '0' | 可反写 |
| 12 | fcanlog | 记录日志 | bpchar | 1 |  | √ | '0' | 记录日志 |
| 13 | ffieldformuladesc | 计算公式别名 | varchar | 500 |  | √ | ' ' | 计算公式别名 |
| 14 | fsourcefieldname | 源单字段 | varchar | 255 |  | √ | ' ' | 源单字段 |
| 15 | ftargetfieldname | 变更单字段名 | varchar | 255 |  | √ | ' ' | 变更单字段名 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fconverttype | 取值 | varchar | 50 |  | √ | ' ' | 取值,枚举: 0 :源单字段 1 :计算公式 |
| 18 | fsumtype | 合并 | varchar | 50 |  | √ | ' ' | 合并,枚举: 0 :取第一行 1 :合计 2 :平均 3 :计数 4 :最大 5 :最小 6 :拼接 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_changemodelfe |  | fentryid |
| 2 | idx_bdtaxr_changemfe_fk |  | fid |

---

## 变更方案-多语言表 t_bdtaxr_changemodel_l

- **表名称：** 变更方案-多语言表
- **表名：** t_bdtaxr_changemodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fareaconditiondesc | 条件描述 | varchar | 2000 |  | √ | ' ' | 条件描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_changemodel_l_0 |  | fid,flocaleid |
| 2 | pk_bdtaxr_changemodel_l |  | fpkid |
