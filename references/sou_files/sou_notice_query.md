# 公告-sou_notice_query

## 公告-多语言表 t_pur_notice_l

- **表名称：** 公告-多语言表
- **表名：** t_pur_notice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 主题 | varchar | 255 |  | √ | ' ' | 主题 |
| 3 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_notice_l_fid |  | fid,flocaleid |
| 2 | t_pur_notice_l_pkey |  | fpkid |

---

## 公告-主表 t_pur_notice

- **表名称：** 公告-主表
- **表名：** t_pur_notice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fbillstatus | 发布状态 | bpchar | 1 |  | √ | ' ' | 发布状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fimportant | fimportant | bpchar | 1 |  | √ | ' ' |  |
| 6 | fbilldate | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 7 | fsupscope | 公告范围 | bpchar | 1 |  | √ | ' ' | 公告范围,枚举: 1 :所有供应商 2 :指定供应商 |
| 8 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 9 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 10 | fistop | fistop | bpchar | 1 |  | √ | '0' |  |
| 11 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 12 | fduedate | 到期时间 | timestamp | 0 |  |  | null | 到期时间 |
| 13 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 14 | ftitle | ftitle | varchar | 255 |  | √ | ' ' |  |
| 15 | fnoticetplid | fnoticetplid | int8 | 64 |  | √ | 0 |  |
| 16 | fbiztype | 公告类型 | bpchar | 1 |  | √ | ' ' | 公告类型,枚举: 1 :询价公告 2 :招标公告 3 :竞价公告 4 :比价公告 5 :中标公告 6 :招募公告 7 :行业动态 8 :系统公告 9 :评估公告 A :询价结果公告 B :竞价结果公告 C :寻源公告 D :流标公告 |
| 17 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 18 | fsourcetype | fsourcetype | int8 | 64 |  | √ | 0 |  |
| 19 | fcontent | 内容 | text | 0 |  |  | null | 内容 |
| 20 | fbillno | 公告编号 | varchar | 80 |  | √ | ' ' | 公告编号 |
| 21 | furgent | furgent | bpchar | 1 |  | √ | ' ' |  |
| 22 | fisallowoperate | fisallowoperate | bpchar | 1 |  | √ | '1' |  |
| 23 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_notice_fbilldate |  | fbilldate |
| 2 | idx_pur_notice_fbillno |  | fbillno |
| 3 | t_pur_notice_pkey |  | fid |
