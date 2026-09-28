# 疑似防重配置-fcs_suspectset

## 疑似防重配置-多语言表 t_fcs_suspectset_l

- **表名称：** 疑似防重配置-多语言表
- **表名：** t_fcs_suspectset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | ffailmessage | 疑似防重校验不通过提示 | varchar | 255 |  | √ | ' ' | 疑似防重校验不通过提示 |
| 5 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 6 | fcheckopname | 目标单据的校验操作 | varchar | 255 |  | √ | ' ' | 目标单据的校验操作 |
| 7 | flandingopname | 目标单据落地的弹框操作 | varchar | 255 |  | √ | ' ' | 目标单据落地的弹框操作 |
| 8 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

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
| 2 | fcheckentityid | 当前单匹配的业务单据 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 3 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 4 | fdestentityid | 当前单据 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 5 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fmessagefield | 疑似防重校验提示字段 | varchar | 50 |  | √ | ' ' | 疑似防重校验提示字段 |
| 10 | flandingop | 当前单据的控制操作 | varchar | 255 |  | √ | ' ' | 当前单据的控制操作,枚举: |
| 11 | fctrltype | 疑似防重控制 | varchar | 30 |  | √ | ' ' | 疑似防重控制,枚举: warning :预警 landing :落地 control :严控 |
| 12 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fchecksignfield | 疑似防重校验标识字段 | varchar | 50 |  | √ | ' ' | 疑似防重校验标识字段 |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcheckopname | 目标单据的校验操作 | varchar | 255 |  | √ | ' ' | 目标单据的校验操作 |
| 20 | fopenmq | 开启MQ消费 | bpchar | 1 |  | √ | '1' | 开启MQ消费 |
| 21 | fcheckop | 当前单据的校验操作 | varchar | 255 |  | √ | ' ' | 当前单据的校验操作,枚举: |
| 22 | ffailmessage | 疑似防重校验不通过提示 | varchar | 255 |  | √ | ' ' | 疑似防重校验不通过提示 |
| 23 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 25 | flandingopname | 目标单据落地的弹框操作 | varchar | 255 |  | √ | ' ' | 目标单据落地的弹框操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcs_suspect |  | fdestentityid,fctrltype |
| 2 | pk_t_fcs_suspectset |  | fid |
