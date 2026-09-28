# 反写规则-msmod_rewriterule

## 反写单据-子表 t_msmod_rewtbillentry

- **表名称：** 反写单据-子表
- **表名：** t_msmod_rewtbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | frewtbill | 反写单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | falias | 核销单据标识 | int8 | 64 |  | √ | 0 | [核销单据类型 msmod_billtype](../mscommon_files/msmod_billtype.md) |
| 6 | frwbeispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_rewtbillentry_fid |  | fid |
| 2 | pk_t_msmod_rewtbillentry |  | fentryid |

---

## 反写公式-子表 t_msmod_rewtformulsub

- **表名称：** 反写公式-子表
- **表名：** t_msmod_rewtformulsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frewtmethod | 反写方式 | varchar | 50 |  | √ | ' ' | 反写方式,枚举: 0 :累加 1 :扣减 2 :覆盖 |
| 2 | fcalformudesc | 计算公式json描述 | varchar | 255 |  | √ | ' ' | 计算公式json描述 |
| 3 | fselectval | 取值方式 | varchar | 50 |  | √ | ' ' | 取值方式,枚举: 0 :核销结果 1 :计算公式 |
| 4 | fwffieldnum | 核销结果字段编码 | varchar | 50 |  | √ | ' ' | 核销结果字段编码 |
| 5 | fcalformudesc_tag | 计算公式json描述_详情 | text | 0 |  |  | null | 计算公式json描述_详情 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcalformula | 计算公式 | varchar | 50 |  | √ | ' ' | 计算公式 |
| 8 | frwfeispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | frewtfieldnum | 反写单据字段编码 | varchar | 50 |  | √ | ' ' | 反写单据字段编码 |
| 10 | fsubrewtbill | 反写单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | frewtfield | 反写单据字段 | varchar | 50 |  | √ | ' ' | 反写单据字段 |
| 14 | fwffield | 核销结果字段 | varchar | 50 |  | √ | ' ' | 核销结果字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_rewtformulsub |  | fdetailid |
| 2 | idx_msmod_rewtformulsub_fentryid |  | fentryid |

---

## 反写规则-多语言表 t_msmod_rewriterule_l

- **表名称：** 反写规则-多语言表
- **表名：** t_msmod_rewriterule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_rewriterule_l_id |  | fid,flocaleid |
| 2 | pk_t_msmod_rewriterule_l |  | fpkid |

---

## 匹配条件-子表 t_msmod_rewtmatchsub

- **表名称：** 匹配条件-子表
- **表名：** t_msmod_rewtmatchsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frefieldnum | 反写单据字段 | varchar | 50 |  | √ | ' ' | 反写单据字段 |
| 2 | fwfbillfieldname | 核销单据字段名称 | varchar | 50 |  | √ | ' ' | 核销单据字段名称 |
| 3 | fcomparison | 比较符 | varchar | 50 |  | √ | ' ' | 比较符,枚举: = :等于 != :不等于 > :大于 < :小于 <= :小于等于 >= :大于等于 |
| 4 | frewtfieldname | 反写单据字段名称 | varchar | 50 |  | √ | ' ' | 反写单据字段名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fwfbill | 核销单据 | int8 | 64 |  | √ | 0 | [核销单据类型 msmod_billtype](../mscommon_files/msmod_billtype.md) |
| 8 | fwfbillfieldnum | 核销单据字段字段 | varchar | 50 |  | √ | ' ' | 核销单据字段字段 |
| 9 | femptyequal | 空值相等匹配 | bpchar | 1 |  | √ | ' ' | 空值相等匹配 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | frwmeispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_rewtmatchsub |  | fdetailid |
| 2 | idx_msmod_rewtmatchsub_fentryid |  | fentryid |

---

## 反写规则-主表 t_msmod_rewriterule

- **表名称：** 反写规则-主表
- **表名：** t_msmod_rewriterule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | frewriteplugin | 反写插件 | varchar | 255 |  | √ | ' ' | 反写插件 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rewriterule_fnumber |  | fnumber |
| 2 | pk_t_msmod_rewriterule |  | fid |

---

## 单据体-子表 t_msmod_rewriteruleentry

- **表名称：** 单据体-子表
- **表名：** t_msmod_rewriteruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frewritemethod | 反写方式 | bpchar | 1 |  | √ | ' ' | 反写方式,枚举: 0 :累加 1 :扣减 |
| 3 | frewritebilllid | 反写单据 | int8 | 64 |  | √ | 0 | [核销单据类型 msmod_billtype](../mscommon_files/msmod_billtype.md) |
| 4 | fbillfieldnumber | 反写单据字段编码 | varchar | 50 |  | √ | ' ' | 反写单据字段编码 |
| 5 | frewritebilllfield | 反写单据字段 | varchar | 50 |  | √ | ' ' | 反写单据字段 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcalculateformula | 计算公式 | varchar | 50 |  | √ | ' ' | 计算公式 |
| 8 | fwriteofffieldnumber | 核销结果字段编码 | varchar | 50 |  | √ | ' ' | 核销结果字段编码 |
| 9 | fcalformuladesc | 计算公式json描述 | varchar | 255 |  | √ | ' ' | 计算公式json描述 |
| 10 | foperationcolumnap | 清除 | varchar | 50 |  | √ | ' ' | 清除 |
| 11 | fcalformuladesc_tag | 计算公式json描述_详情 | text | 0 |  |  | null | 计算公式json描述_详情 |
| 12 | fselectvalue | 取值 | bpchar | 1 |  | √ | ' ' | 取值,枚举: 0 :核销结果 1 :计算公式 |
| 13 | fwriteofffield | 核销结果字段 | varchar | 50 |  | √ | ' ' | 核销结果字段 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rewriteruleentry_fid |  | fid |
| 2 | pk_t_msmod_rewriteruleentry |  | fentryid |
