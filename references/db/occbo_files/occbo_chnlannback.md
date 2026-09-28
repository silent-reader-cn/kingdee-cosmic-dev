# 渠道公告反馈信息-occbo_chnlannback

## 渠道公告反馈信息-主表 t_occbo_chnlannfeedback

- **表名称：** 渠道公告反馈信息-主表
- **表名：** t_occbo_chnlannfeedback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 公告主题 | varchar | 255 |  | √ | ' ' | 公告主题 |
| 3 | fcreatorid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fannclassid | 公告分类 | int8 | 64 |  | √ | 0 | [公告分类 occbo_reportclass](../occbo_files/occbo_reportclass.md) |
| 5 | fcontent_tag | 反馈内容_详情 | text | 0 |  |  | null | 反馈内容_详情 |
| 6 | fcreatetime | 反馈时间 | timestamp | 0 |  |  | null | 反馈时间 |
| 7 | fcontent | 反馈内容 | varchar | 255 |  | √ | ' ' | 反馈内容 |
| 8 | fbillno | 公告编号 | varchar | 80 |  | √ | ' ' | 公告编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_chlannfeedback_num |  | fbillno |
| 2 | pk_occbo_chnlannfeedback |  | fid |
| 3 | idx_occbo_chlannfeedback_time |  | fcreatetime |
| 4 | idx_occbo_chlannfeedback_class |  | fannclassid |
