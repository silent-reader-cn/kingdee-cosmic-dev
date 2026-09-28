# 人员信息清除记录-bos_user_clean

## 人员信息清除记录-主表 t_sec_userclean

- **表名称：** 人员信息清除记录-主表
- **表名：** t_sec_userclean

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcleantime | 清除时间 | timestamp | 0 |  |  | null | 清除时间 |
| 3 | fcleanerid | 清除人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fuserid | 人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fuserinfocleanschemeid | 人员信息清理方案 | int8 | 64 |  | √ | 0 | 人员个人信息清除方案 bos_user_infocleanscheme |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sec_userclean |  | fid |
| 2 | idx_t_sec_userclean |  | fuserinfocleanschemeid |
