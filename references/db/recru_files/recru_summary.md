# 招聘总结-recru_summary

## 发布渠道-多选基础资料表 t_recru_publishchannel

- **表名称：** 发布渠道-多选基础资料表
- **表名：** t_recru_publishchannel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [渠道管理 recru_channel](../recru_files/recru_channel.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_publishchannel |  | fpkid |
| 2 | idx_recru_publishchannel |  | fid |

---

## 招聘总结-主表 t_recru_summary

- **表名称：** 招聘总结-主表
- **表名：** t_recru_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | finterviewreport | AI面试报告生成总次数 | int4 | 32 |  | √ | 0 | AI面试报告生成总次数 |
| 6 | fintervewinvitation | 面试邀约总次数 | int4 | 32 |  | √ | 0 | 面试邀约总次数 |
| 7 | finterviewcount | AI面试开展总次数 | int4 | 32 |  | √ | 0 | AI面试开展总次数 |
| 8 | fportraitcount | 职位画像生成次数 | int4 | 32 |  | √ | 0 | 职位画像生成次数 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | foutercount | 金蝶云星瀚外部人才库 | int4 | 32 |  | √ | 0 | 金蝶云星瀚外部人才库 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fmatchcount | 人岗匹配总人次 | int4 | 32 |  | √ | 0 | 人岗匹配总人次 |
| 15 | finnercount | 金蝶云星瀚员工人才库 | int4 | 32 |  | √ | 0 | 金蝶云星瀚员工人才库 |
| 16 | fjdcount | jd生成次数 | int4 | 32 |  | √ | 0 | jd生成次数 |
| 17 | fsession | 会话 | varchar | 50 |  | √ | ' ' | 会话 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_summary |  | fid |
| 2 | idx_recru_summary_session |  | fsession |

---

## 招聘总结-多语言表 t_recru_summary_l

- **表名称：** 招聘总结-多语言表
- **表名：** t_recru_summary_l

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
| 1 | pk_recru_summary_l |  | fpkid |
| 2 | idx__recru_summary_l |  | fid,flocaleid |

---

## 简历渠道下载明细-子表 t_recru_downloaddetail

- **表名称：** 简历渠道下载明细-子表
- **表名：** t_recru_downloaddetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 下载类型 | varchar | 10 |  | √ | ' ' | 下载类型,枚举: 1 :主动投递下载 2 :搜索下载 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道管理 recru_channel](../recru_files/recru_channel.md) |
| 5 | fdownloadcount | 下载数量 | int4 | 32 |  | √ | 0 | 下载数量 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_downloaddetail |  | fentryid |
| 2 | idx_recru_downloaddetail |  | fid |
