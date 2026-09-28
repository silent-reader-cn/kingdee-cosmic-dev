# 邀约注册消息配置-srm_rfimsgconfig

## 邀约注册消息配置-主表 t_srm_rfimsgconfig

- **表名称：** 邀约注册消息配置-主表
- **表名：** t_srm_rfimsgconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpreinsertdata | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 6 | fphonemessage | 短信消息 | varchar | 255 |  | √ | ' ' | 短信消息 |
| 7 | frichbigtext | 消息文本 | text | 0 |  |  | null | 消息文本 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | frichbigtext_tag | 消息文本_详情 | text | 0 |  |  | null | 消息文本_详情 |
| 10 | fdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | ftpllanguageid | 模板语言 | int8 | 64 |  | √ | 0 | [语言 inte_enabledlanguage](../base_files/inte_enabledlanguage.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsendphonemsg | 发送短信 | bpchar | 1 |  | √ | '0' | 发送短信 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | femailtitle | 邮件标题 | varchar | 255 |  | √ | ' ' | 邮件标题 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_rfimsgconfig_fnum |  | fnumber |
| 2 | pk_srm_rfimsgconfig |  | fid |

---

## 邀约注册消息配置-多语言表 t_srm_rfimsgconfig_l

- **表名称：** 邀约注册消息配置-多语言表
- **表名：** t_srm_rfimsgconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_rfimsg_l_fid_flocaleid |  | fid,flocaleid |
| 2 | pk_srm_rfimsgconfig_l |  | fpkid |
