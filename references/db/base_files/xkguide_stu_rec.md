# 指引学习完成记录-xkguide_stu_rec

## 指引学习完成记录-主表 t_xkbase_guide_stu_rec

- **表名称：** 指引学习完成记录-主表
- **表名：** t_xkbase_guide_stu_rec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstudystatus | 学习状态 | varchar | 5 |  | √ | '0' | 学习状态,枚举: |
| 3 | fguidestepid | 指引步骤 | int8 | 64 |  | √ | 0 | 指引步骤 xkguide_step |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | forgid | 业务单元 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbase_guide_stu_rec |  | fid |
| 2 | idx_guide_stu_rec_step |  | fguidestepid |
