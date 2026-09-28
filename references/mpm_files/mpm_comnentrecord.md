# 评论记录-mpm_comnentrecord

## 评论记录-主表 t_mpm_comment

- **表名称：** 评论记录-主表
- **表名：** t_mpm_comment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fparentid | 父评论单据id | int8 | 64 |  | √ | 0 | 父评论单据id |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fimagepath | 图片路径 | varchar | 1000 |  | √ | ' ' | 图片路径 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 11 | fbizobjid | 业务对象 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_comment_fbillno |  | fbillno |
| 2 | idx_mpm_comment_fid |  | fid |
| 3 | pk_mpm_comment |  | fid |

---

## 评论记录-分表 t_mpm_comment_a

- **表名称：** 评论记录-分表
- **表名：** t_mpm_comment_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontent_tag | 评论内容_详情 | text | 0 |  | √ | ' ' | 评论内容_详情 |
| 3 | fcontent | 评论内容 | varchar | 255 |  | √ | ' ' | 评论内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_comment_a_f |  | fid |
| 2 | pk_mpm_comment_a |  | fid |
