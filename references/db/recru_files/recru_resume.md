# 简历库-recru_resume

## 个人亮点-子表 t_recru_goodpoint

- **表名称：** 个人亮点-子表
- **表名：** t_recru_goodpoint

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodpointdesc | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fgoodpointlabel | 标签 | varchar | 255 |  | √ | ' ' | 标签 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_goodpoint |  | fentryid |
| 2 | idx_recru_goodpoint_fid |  | fid |

---

## 简历库-多语言表 t_recru_resume_l

- **表名称：** 简历库-多语言表
- **表名：** t_recru_resume_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_resume_l |  | fpkid |
| 2 | idx_recru_resume_l |  | fid,flocaleid |

---

## 特别关注单据体-子表 t_recru_focuspoint

- **表名称：** 特别关注单据体-子表
- **表名：** t_recru_focuspoint

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | ffocuslabel | 标签 | varchar | 255 |  | √ | ' ' | 标签 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | ffocusdesc | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_focuspoint |  | fentryid |
| 2 | idx_recru_focuspoint_fid |  | fid |

---

## 简历库-主表 t_recru_resume

- **表名称：** 简历库-主表
- **表名：** t_recru_resume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcondensedresume | 候选人精简简历 | varchar | 255 |  | √ | ' ' | 候选人精简简历 |
| 3 | fuploadtime | 上传时间 | timestamp | 0 |  |  | null | 上传时间 |
| 4 | fworkingseniority | 工龄 | numeric | 23 | 10 | √ | 0 | 工龄 |
| 5 | flastemployer | 最近一次任职公司 | varchar | 255 |  | √ | ' ' | 最近一次任职公司 |
| 6 | fdistrichannelid | 发布渠道 | int8 | 64 |  | √ | 0 | [渠道管理 recru_channel](../recru_files/recru_channel.md) |
| 7 | fcondensedresume_tag | 候选人精简简历_详情 | text | 0 |  |  | null | 候选人精简简历_详情 |
| 8 | fgenerationtype | 简历生成方式 | varchar | 50 |  | √ | ' ' | 简历生成方式,枚举: originupload :原件上传 textupload :文本上传 api :接口 |
| 9 | freschannelid | 招聘渠道 | int8 | 64 |  | √ | 0 | [简历渠道 recru_reschannel](../recru_files/recru_reschannel.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fnation | 民族 | varchar | 50 |  | √ | ' ' | 民族 |
| 12 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fparsestatus | 简历解析状态 | varchar | 2 |  | √ | ' ' | 简历解析状态,枚举: A :解析中 B :已完成 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcontactemail | 电子邮件 | varchar | 255 |  | √ | ' ' | 电子邮件 |
| 17 | fpostalcode | 邮政编码 | varchar | 20 |  | √ | ' ' | 邮政编码 |
| 18 | fcity | 城市 | varchar | 50 |  | √ | ' ' | 城市 |
| 19 | flastjobtitle | 最近一次任职岗位 | varchar | 255 |  | √ | ' ' | 最近一次任职岗位 |
| 20 | fresumechannelurl | 招聘渠道简历详情页面url | varchar | 1000 |  | √ | ' ' | 招聘渠道简历详情页面url |
| 21 | fclientparsestatus | 客户端上传简历解析状态 | varchar | 2 |  | √ | ' ' | 客户端上传简历解析状态,枚举: 10 :解析中 20 :解析完成 |
| 22 | fpolitical | 政治面貌 | varchar | 50 |  | √ | ' ' | 政治面貌 |
| 23 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fbirthday | 出生日期 | timestamp | 0 |  |  | null | 出生日期 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fgender | 性别 | varchar | 2 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 3 :未知 |
| 28 | fregisteredresidence | 户口所在地 | varchar | 128 |  | √ | ' ' | 户口所在地 |
| 29 | ftopeducation | 最高学历 | varchar | 50 |  | √ | ' ' | 最高学历 |
| 30 | fstructresumeid | 结构化简历 | int8 | 64 |  | √ | 0 | [结构化简历 recru_structresume](../recru_files/recru_structresume.md) |
| 31 | fmarital | 婚姻状况 | varchar | 50 |  | √ | ' ' | 婚姻状况 |
| 32 | fsessionid | 客户端会话ID | varchar | 50 |  | √ | ' ' | 客户端会话ID |
| 33 | fdownloadtype | 下载方式 | varchar | 50 |  | √ | ' ' | 下载方式,枚举: 1 :主动投递下载 2 :搜索下载 |
| 34 | fdateofbirth | 出生日期 | varchar | 50 |  | √ | ' ' | 出生日期 |
| 35 | fpersonid | 身份证号码 | varchar | 18 |  | √ | ' ' | 身份证号码 |
| 36 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | fnativeplace | 籍贯 | varchar | 255 |  | √ | ' ' | 籍贯 |
| 38 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 39 | fcellphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 40 | fsummary | 一句话总结 | varchar | 255 |  | √ | ' ' | 一句话总结 |
| 41 | fcountry | 国家 | varchar | 50 |  | √ | ' ' | 国家 |
| 42 | fstructstatus | 结构化状态 | varchar | 2 |  | √ | ' ' | 结构化状态,枚举: 10 :结构化中 20 :结构化成功 30 :结构化失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_resume_sessionid |  | fsessionid |
| 2 | pk_recru_resume |  | fid |
