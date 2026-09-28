# 疑似防重配置-fcs_suspectset

## 疑似防重配置-多语言表 t_fcs_suspectset_l

- **表名称：** 疑似防重配置-多语言表
- **表名：** t_fcs_suspectset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmainorgfieldname | 当前单据的主业务组织字段 | varchar | 255 |  | √ | ' ' | 当前单据的主业务组织字段 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | ffailmessage | 疑似防重校验不通过提示 | varchar | 255 |  | √ | ' ' | 疑似防重校验不通过提示 |
| 6 | fbizdatefieldname | 当前单据的业务日期字段 | varchar | 255 |  | √ | ' ' | 当前单据的业务日期字段 |
| 7 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 8 | fcheckopname | 目标单据的校验操作 | varchar | 255 |  | √ | ' ' | 目标单据的校验操作 |
| 9 | flandingopname | 目标单据落地的弹框操作 | varchar | 255 |  | √ | ' ' | 目标单据落地的弹框操作 |
| 10 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcs_suspect_l |  | fid,flocaleid |
| 2 | pk_t_fcs_suspectset_l |  | fpkid |

---

## 匹配方案-子表 t_fcs_suspectset_m

- **表名称：** 匹配方案-子表
- **表名：** t_fcs_suspectset_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdestfilterrecord | 当前单适用条件记录 | varchar | 255 |  | √ | ' ' | 当前单适用条件记录 |
| 3 | fmatchrecord | 匹配方案记录 | varchar | 255 |  | √ | ' ' | 匹配方案记录 |
| 4 | fdestfilter | 当前单适用条件 | varchar | 50 |  | √ | ' ' | 当前单适用条件 |
| 5 | fcheckfilterrecord | 业务单据适用条件记录 | varchar | 255 |  | √ | ' ' | 业务单据适用条件记录 |
| 6 | fcheckfilterrecord_tag | 业务单据适用条件记录_详情 | text | 0 |  |  | null | 业务单据适用条件记录_详情 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmatchrecord_tag | 匹配方案记录_详情 | text | 0 |  |  | null | 匹配方案记录_详情 |
| 9 | fcheckfilter | 业务单据适用条件 | varchar | 50 |  | √ | ' ' | 业务单据适用条件 |
| 10 | fdestfilterrecord_tag | 当前单适用条件记录_详情 | text | 0 |  |  | null | 当前单适用条件记录_详情 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fmatchscheme | 疑似重复匹配方案 | varchar | 50 |  | √ | ' ' | 疑似重复匹配方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcs_suspect_m |  | fid |
| 2 | pk_t_fcs_suspectset_m |  | fentryid |

---

## 疑似防重配置-主表 t_fcs_suspectset

- **表名称：** 疑似防重配置-主表
- **表名：** t_fcs_suspectset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckentityid | 当前单匹配的业务单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 3 | fusestatus | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: create :创建中 apply :已生效 change :变更中 |
| 4 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 5 | fbizdatefieldname | 当前单据的业务日期字段 | varchar | 255 |  | √ | ' ' | 当前单据的业务日期字段 |
| 6 | fdestentityid | 当前单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 7 | fispreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 8 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmainorgfieldname | 当前单据的主业务组织字段 | varchar | 255 |  | √ | ' ' | 当前单据的主业务组织字段 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fmessagefield | 疑似防重校验提示字段 | varchar | 50 |  | √ | ' ' | 疑似防重校验提示字段 |
| 14 | flandingop | 当前单据的控制操作 | varchar | 255 |  | √ | ' ' | 当前单据的控制操作,枚举: |
| 15 | fctrltype | 疑似防重控制 | varchar | 30 |  | √ | ' ' | 疑似防重控制,枚举: warning :预警 landing :落地 control :严控 |
| 16 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fchecksignfield | 疑似防重校验标识字段 | varchar | 50 |  | √ | ' ' | 疑似防重校验标识字段 |
| 18 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 19 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 22 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fcheckopname | 目标单据的校验操作 | varchar | 255 |  | √ | ' ' | 目标单据的校验操作 |
| 24 | fopenmq | 开启MQ消费 | bpchar | 1 |  | √ | '1' | 开启MQ消费 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fmainorgfield | 当前单据的主业务组织字段 | varchar | 50 |  | √ | ' ' | 当前单据的主业务组织字段,枚举: |
| 27 | fbizdatefield | 当前单据的业务日期字段 | varchar | 50 |  | √ | ' ' | 当前单据的业务日期字段,枚举: |
| 28 | fcheckop | 当前单据的校验操作 | varchar | 255 |  | √ | ' ' | 当前单据的校验操作,枚举: |
| 29 | ffailmessage | 疑似防重校验不通过提示 | varchar | 255 |  | √ | ' ' | 疑似防重校验不通过提示 |
| 30 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 32 | flandingopname | 目标单据落地的弹框操作 | varchar | 255 |  | √ | ' ' | 目标单据落地的弹框操作 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcs_suspect |  | fdestentityid,fctrltype |
| 2 | pk_t_fcs_suspectset |  | fid |
