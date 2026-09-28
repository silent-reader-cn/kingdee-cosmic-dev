# 渠道公告-occbo_channelannoun

## 渠道公告-多语言表 t_occbo_ch_announce_l

- **表名称：** 渠道公告-多语言表
- **表名：** t_occbo_ch_announce_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 公告主题 | varchar | 80 |  | √ | ' ' | 公告主题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_ch_announce_l |  | fpkid |
| 2 | idx_occbo_ch_announ_flid |  | fid,flocaleid |

---

## 渠道单据体-子表 t_occbo_ch_announce_ch

- **表名称：** 渠道单据体-子表
- **表名：** t_occbo_ch_announce_ch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fchannelid | 渠道编码 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 4 | fsaleorgid | 销售组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_announce_ch_fid |  | fid |
| 2 | pk_occbo_ch_announce_ch |  | fentryid |

---

## 渠道公告-主表 t_occbo_ch_announce

- **表名称：** 渠道公告-主表
- **表名：** t_occbo_ch_announce

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 公告分类 | int8 | 64 |  | √ | 0 | 公告分类 occbo_reportclass |
| 3 | fusergroup | 用户单选按钮组 | bpchar | 1 |  | √ | ' ' | 用户单选按钮组,枚举: 1 :全部用户 2 :指定用户 |
| 4 | fpublishtime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 5 | fchannelgroup | 渠道单选按钮组 | bpchar | 1 |  | √ | ' ' | 渠道单选按钮组,枚举: 1 :全部渠道 2 :指定渠道 3 :指定销售组织 |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fuserbutton | 按用户发布 | bpchar | 1 |  | √ | '0' | 按用户发布 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcategary | fcategary | varchar | 255 |  | √ | ' ' |  |
| 10 | fstatus | 公告状态 | bpchar | 1 |  | √ | 'A' | 公告状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fdescription_tag | 公告信息_详情 | text | 0 |  |  | null | 公告信息_详情 |
| 15 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 16 | fpublisherid | 发布人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillno | fbillno | varchar | 80 |  | √ | ' ' |  |
| 18 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fname | 公告主题 | varchar | 255 |  | √ | ' ' | 公告主题 |
| 21 | fpublishstatus | 发布状态 | bpchar | 1 |  | √ | '0' | 发布状态,枚举: 0 :未发布 1 :已发布 |
| 22 | fchannelbutton | 按渠道发布 | bpchar | 1 |  | √ | '0' | 按渠道发布 |
| 23 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'A' |  |
| 24 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 25 | fdescription | 公告信息 | varchar | 255 |  | √ | ' ' | 公告信息 |
| 26 | ftopic | ftopic | varchar | 255 |  | √ | ' ' |  |
| 27 | fscanqty | 阅读量 | int4 | 32 |  | √ | 0 | 阅读量 |
| 28 | ffeedback | 反馈量 | int4 | 32 |  | √ | 0 | 反馈量 |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fpublishdate | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 31 | fnumber | 公告编号 | varchar | 80 |  | √ | ' ' | 公告编号 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_announce_num |  | fbillno |
| 2 | pk_occbo_ch_announce |  | fid |

---

## 用户单据体-子表 t_occbo_ch_announce_user

- **表名称：** 用户单据体-子表
- **表名：** t_occbo_ch_announce_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fusernumber | 工号 | varchar | 80 |  | √ | ' ' | 工号 |
| 4 | fuserid | 姓名 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_ch_announce_user |  | fentryid |
| 2 | idx_occbo_ch_announce_u_fid |  | fid |
