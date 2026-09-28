# 渠道公告-occbo_channelannounce

## 渠道单据体-子表 t_occbo_ch_announce_ch

- **表名称：** 渠道单据体-子表
- **表名：** t_occbo_ch_announce_ch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fchannelid | 渠道编码 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 4 | fsaleorgid | fsaleorgid | int8 | 64 |  | √ | 0 |  |
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
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fusergroup | fusergroup | bpchar | 1 |  | √ | ' ' |  |
| 4 | fpublishtime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 5 | fchannelgroup | fchannelgroup | bpchar | 1 |  | √ | ' ' |  |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fuserbutton | 按用户发布 | bpchar | 1 |  | √ | '0' | 按用户发布 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcategary | 公告分类 | varchar | 255 |  | √ | ' ' | 公告分类 |
| 10 | fstatus | fstatus | bpchar | 1 |  | √ | 'A' |  |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 14 | fdescription_tag | 公告信息_详情 | text | 0 |  |  | null | 公告信息_详情 |
| 15 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 16 | fpublisherid | 发布人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillno | 公告编号 | varchar | 80 |  | √ | ' ' | 公告编号 |
| 18 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 21 | fpublishstatus | 发布状态 | bpchar | 1 |  | √ | '0' | 发布状态,枚举: 0 :未发布 1 :已发布 |
| 22 | fchannelbutton | 按渠道发布 | bpchar | 1 |  | √ | '0' | 按渠道发布 |
| 23 | fbillstatus | 公告状态 | bpchar | 1 |  | √ | 'A' | 公告状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 25 | fdescription | 公告信息 | varchar | 255 |  | √ | ' ' | 公告信息 |
| 26 | ftopic | 公告主题 | varchar | 255 |  | √ | ' ' | 公告主题 |
| 27 | fscanqty | fscanqty | int4 | 32 |  | √ | 0 |  |
| 28 | ffeedback | ffeedback | int4 | 32 |  | √ | 0 |  |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fpublishdate | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 31 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
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
