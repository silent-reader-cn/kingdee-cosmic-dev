# 对话反馈列表-cbi_chat_feedback

## 对话反馈列表-主表 t_cbi_chat_feedback

- **表名称：** 对话反馈列表-主表
- **表名：** t_cbi_chat_feedback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 反馈时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 反馈时间 |
| 3 | fimrecordid | 对话id | int8 | 64 |  | √ | 0 | 对话id |
| 4 | fcontenttype | 反馈类型 | varchar | 64 |  | √ | ' ' | 反馈类型,枚举: 0 :查数理解出错 1 :数据错误 2 :分析不专业 3 :其他 5 :/ |
| 5 | fcontent | 反馈内容 | varchar | 2000 |  |  | ' ' | 反馈内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_feedback |  | fid |
| 2 | t_cbi_chat_feedback_fimrecordid_idx |  | fimrecordid |
