# 冻结服务配置-msmod_freezesetting

## 冻结服务配置-主表 t_msmod_freezesetting

- **表名称：** 冻结服务配置-主表
- **表名：** t_msmod_freezesetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 服务名称 | int8 | 64 |  | √ | 0 | 冻结配置类型 msmod_freezetype |
| 5 | fbizapp | 所属应用 | varchar | 50 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 6 | fbillopnumber | 单据操作 | varchar | 255 |  | √ | ' ' | 单据操作,枚举: |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fissysinit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 11 | fproviderentityid | 供应实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 12 | fbillopname | 操作名称 | varchar | 255 |  | √ | ' ' | 操作名称 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | ffilterjson | 通用过滤json | varchar | 255 |  | √ | ' ' | 通用过滤json |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fenable | 启用 | varchar | 50 |  | √ | '1' | 启用,枚举: 0 :禁用 1 :可用 |
| 19 | ffilterformula_tag | 通用过滤表达式_详情 | text | 0 |  |  | null | 通用过滤表达式_详情 |
| 20 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | ffreezeobjid | 冻结/解冻单据 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 23 | ffilterjson_tag | 通用过滤json_详情 | text | 0 |  |  | null | 通用过滤json_详情 |
| 24 | ffilterformula | 通用过滤表达式 | varchar | 255 |  | √ | ' ' | 通用过滤表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_freezesetting_num |  | fnumber |
| 2 | pk_t_msmod_freezesetting |  | fid |

---

## 冻结服务配置-多语言表 t_msmod_freezesetting_l

- **表名称：** 冻结服务配置-多语言表
- **表名：** t_msmod_freezesetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 50 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fbillopname | 操作名称 | varchar | 255 |  | √ | ' ' | 操作名称 |
| 7 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_freezesetting_l_fid |  | fid,flocaleid |
| 2 | pk_t_msmod_freezesetting_l |  | fpkid |
