# 指引步骤关联链接状态记录-xkguide_ref_stu_rec

## 指引步骤关联链接状态记录-主表 t_xkbase_guide_ref_rec

- **表名称：** 指引步骤关联链接状态记录-主表
- **表名：** t_xkbase_guide_ref_rec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 完成状态 | varchar | 10 |  | √ | '1' | 完成状态,枚举: 0 :未开始 1 :已完成 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fguiderefid | 指引关联 | int8 | 64 |  | √ | 0 | [指引步骤关联页面/表单 xkguide_ref](../xkbase_files/xkguide_ref.md) |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbase_guide_ref_rec |  | fid |
| 2 | idx_ref_rec_ref_id |  | fguiderefid |
